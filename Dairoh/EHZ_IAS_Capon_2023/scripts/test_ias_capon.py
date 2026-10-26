"""Numerical regression against the scalar quadratic form in Gal's C kernel,
plus a synthetic known-direction plane wave and distortionless reconstruction."""
import json
import numpy as np
from ias_capon_numpy import ias_capon,power_scan,prepare_inverse,covariances,beams
rng=np.random.default_rng(27)
xy=np.array([[-.12,.10],[.16,.11],[-.07,-.12],[.18,-.08],[.04,.21]])
fs=25.;t=np.arange(2000)/fs;injected=np.array([.25,.40]);freqs=np.arange(1.25,8,.25);ph=rng.uniform(0,2*np.pi,len(freqs));x=[]
for pos in xy:
 signal=np.sum(np.cos(2*np.pi*freqs[:,None]*(t+pos@injected)[None,:]+ph[:,None]),axis=0)
 x.append(signal+rng.normal(0,.3,len(t)))
x=np.array(x);r=ias_capon(x,xy,limit=.8,step=.025)
assert np.allclose([r['sx'],r['sy']],injected,atol=.026),r
R,f,n,nwin=covariances(x);sel=(f>=1)&(f<=8);inv=prepare_inverse(R[sel],n,1);points=np.array([[.25,.4],[-.3,.2],[.1,-.2]])
vec=power_scan(inv,f[sel],xy,points);scalar=[]
for sx,sy in points:
 total=0.
 for I,ff in zip(inv,f[sel]):
  den=I.diagonal().real.sum()
  for m in range(5):
   for q in range(m+1,5):
    arg=-2*np.pi*ff*(sx*(xy[m,0]-xy[q,0])+sy*(xy[m,1]-xy[q,1]))
    den+=2*(I[m,q].real*np.cos(arg)-I[m,q].imag*np.sin(arg))
  total+=1/den
 scalar.append(total)
assert np.allclose(vec,scalar,rtol=1e-9,atol=1e-10)
mv,ds=beams(x,xy,r);assert np.isfinite(mv).all() and len(mv)==len(t)
# Pure plane wave must reconstruct the known reference waveform, not reverse BAZ.
truth=np.sum(np.cos(2*np.pi*freqs[:,None]*t[None,:]+ph[:,None]),axis=0)
corr=float(np.corrcoef(mv[100:-100],truth[100:-100])[0,1]);assert corr>.97,corr
print(json.dumps({'scalar_vs_vector_max_error':float(np.max(abs(vec-scalar))),'injected_slowness_s_per_km':injected.tolist(),'recovered_slowness_s_per_km':[r['sx'],r['sy']],'recovered_baz_deg':r['baz'],'mvdr_truth_correlation':corr,'snapshots':nwin,'status':'PASS'},indent=2))
