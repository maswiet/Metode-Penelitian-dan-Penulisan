"""NumPy implementation of Martin Gal's IAS-Capon numerical procedure.
Reference: mgalcode/IAS-Capon, subroutines.py::IAS_Capon,
commit f9290415279a6cc372d4fc0d9eafa2d9bf4c0352 (Python 2/scipy.weave).
Coordinates here are east/north km and slowness is s/km; upstream uses degrees
and s/degree. This module uses the same per-bin whitening, trace/nsamp loading,
frequency-dependent steering and INCOHERENT summation of inverse quadratic forms.
MVDR waveform synthesis is an explicitly separate extension, not upstream output.
"""
import numpy as np
from scipy.signal import stft,istft


def covariances(x,fs=25.,seconds=4.):
    n=int(round(fs*seconds));hop=n//2
    starts=range(0,x.shape[1]-n+1,hop)
    segments=np.stack([x[:,i:i+n] for i in starts],axis=0)
    segments=(segments-segments.mean(axis=-1,keepdims=True))*np.hanning(n)
    spectra=np.fft.rfft(segments,axis=-1)
    R=np.einsum('wif,wjf->fij',spectra,spectra.conj())/len(segments)
    return R,np.fft.rfftfreq(n,1/fs),n,len(segments)


def prepare_inverse(R,n,dl):
    scales=np.sqrt(np.maximum(np.real(np.diagonal(R,axis1=1,axis2=2)),np.finfo(float).tiny))
    W=R/(scales[:,:,None]*scales[:,None,:])
    # Original IAS-Capon loads AFTER per-frequency station whitening.
    load=np.trace(W,axis1=1,axis2=2).real/n*dl
    W=W+load[:,None,None]*np.eye(R.shape[1])[None]
    return np.linalg.inv(W)


def power_scan(inv,freq,xy,points):
    delays=points@xy.T
    power=np.zeros(len(points))
    for f,I in zip(freq,inv):
        a=np.exp(2j*np.pi*f*delays)
        den=np.einsum('gi,ij,gj->g',a.conj(),I,a).real
        if np.any(den<=0):raise ValueError('nonpositive Capon denominator')
        power+=1/den
    return power


def ias_capon(x,xy,fs=25.,low=1.,high=8.,dl=1.,limit=3.,step=.05):
    R,freq,n,nwin=covariances(x,fs)
    if nwin<=len(x):raise ValueError('need more snapshots than stations')
    use=(freq>=low)&(freq<=high)
    axis=np.arange(-limit,limit+step*.5,step)
    sx,sy=np.meshgrid(axis,axis,indexing='ij');points=np.c_[sx.ravel(),sy.ravel()]
    inv=prepare_inverse(R[use],n,dl)
    P=power_scan(inv,freq[use],xy,points)
    k=int(np.argmax(P));slow=points[k];norm=np.linalg.norm(slow)
    baz=float(np.degrees(np.arctan2(slow[0],slow[1]))%360) if norm>1e-8 else None
    return {'sx':float(slow[0]),'sy':float(slow[1]),'baz':baz,'velocity':float(1/norm) if norm>1e-8 else None,'boundary':bool(np.any(np.isclose(abs(slow),limit))), 'near_zero_slowness':bool(norm<.075),'snapshots':nwin,'axis':axis,'power_db':(10*np.log10(P/P.max())).reshape(sx.shape),'R':R,'freq':freq,'nsamp':n}


def beams(x,xy,fit,fs=25.,dl=1.):
    """Return MVDR and delay-sum at IAS DOA. Fit RAW-count CSD, without the
    direction-scan whitening, so the reconstruction is distortionless in counts.
    Fixed weights are applied by STFT/ISTFT. No time-window-varying DOA chasing.
    """
    n=fit['nsamp'];R=fit['R'].copy();f=fit['freq'];slow=np.array([fit['sx'],fit['sy']])
    R+= (np.trace(R,axis1=1,axis2=2).real/n*dl)[:,None,None]*np.eye(len(x))[None]
    a=np.exp(2j*np.pi*f[:,None]*(xy@slow)[None,:])
    inva=np.linalg.solve(R,a[:,:,None])[:,:,0]
    w=inva/np.einsum('fi,fi->f',a.conj(),inva)[:,None]
    if not np.allclose(np.einsum('fi,fi->f',w.conj(),a),1,atol=1e-8):raise AssertionError('MVDR gain not unity')
    _,times,Z=stft(x,fs=fs,window='hann',nperseg=n,noverlap=n//2,boundary='zeros',padded=True,axis=-1)
    Ym=np.einsum('fi,ift->ft',w.conj(),Z)
    Yd=np.einsum('fi,ift->ft',a.conj()/len(x),Z)
    use=(f>=.5)&(f<=10);Ym[~use]=0;Yd[~use]=0
    _,mv=istft(Ym,fs=fs,window='hann',nperseg=n,noverlap=n//2,boundary=True)
    _,ds=istft(Yd,fs=fs,window='hann',nperseg=n,noverlap=n//2,boundary=True)
    return mv[:x.shape[1]],ds[:x.shape[1]]
