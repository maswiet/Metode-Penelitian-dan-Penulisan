"""Re-read original EHZ MiniSEED, cut conservative candidates and run IAS-Capon.
Usage: python analyze_events.py --archive /path/to/AM --candidates candidates.csv
       --qc-metrics previous-event-metrics.jsonl [--limit 1]
"""
import argparse,csv,json,hashlib,datetime as dt,sys
from pathlib import Path
import numpy as np
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.signal import butter,sosfiltfilt,resample_poly,spectrogram
from scipy.ndimage import uniform_filter1d
from obspy import read,Stream,Trace,UTCDateTime
from obspy.geodetics import gps2dist_azimuth
from ias_capon_numpy import ias_capon,beams
ST=[('UGM01','RE5DE',-7.692254,110.438530),('UGM02','R6940',-7.692179,110.441112),('UGM03','R265F',-7.6942892743868265,110.43897691637302),('UGM04','R7D17',-7.693931,110.441316),('UGM05','R0279',-7.691258,110.440031)]
OUT=Path(__file__).resolve().parents[1];FS=25.
xy=[]
for _,_,lat,lon in ST:
 d,az,_=gps2dist_azimuth(ST[0][2],ST[0][3],lat,lon);xy.append([d/1000*np.sin(np.deg2rad(az)),d/1000*np.cos(np.deg2rad(az))])
xy=np.array(xy);xy-=xy.mean(axis=0)

def load_cut(root,t,end):
 start=t-60; finish=t+end
 raw=Stream();arr=[]
 for label,st,lat,lon in ST:
  s=Stream()
  first=UTCDateTime((start-10).date);last=UTCDateTime((finish+10).date)
  day=first
  while day<=last:
   p=root/st/'EHZ.D'/f'AM.{st}.00.EHZ.D.{day.year}.{day.julday:03d}'
   if p.exists():s+=read(str(p),starttime=start-10,endtime=finish+10)
   day+=86400
  s=s.select(network='AM',station=st,channel='EHZ');s.merge(method=0,fill_value=None)
  if len(s)!=1:raise ValueError(st+': no unique trace')
  tr=s[0]
  if tr.stats.sampling_rate!=100:raise ValueError(st+': unexpected sampling rate')
  if tr.stats.starttime>start-3 or tr.stats.endtime<finish+3:raise ValueError(st+': incomplete expanded cut')
  if np.ma.isMaskedArray(tr.data) and np.any(tr.data.mask):raise ValueError(st+': gap or conflicting overlap in expanded cut')
  v=tr.data.astype(float);n=len(v);edges=np.r_[0,np.flatnonzero(np.diff(v)!=0)+1,n]
  if np.any(np.diff(edges)>=20):raise ValueError(st+': raw repeated-value run >=0.2 s')
  if np.any(abs(v)>=8388600):raise ValueError(st+': potential 24-bit rail')
  cut=tr.copy().trim(starttime=start,endtime=finish,nearest_sample=False);raw+=cut
  # Filter with 10 seconds of original context, then anti-alias decimate.
  yf=sosfiltfilt(butter(4,[.5,10],btype='bandpass',fs=100,output='sos'),v-v.mean())
  yd=resample_poly(yf,1,4);offset=float(tr.stats.starttime-start)
  target=np.arange(int(round((end+60)*FS))+1)/FS
  aligned=np.interp(target,offset+np.arange(len(yd))/FS,yd)
  arr.append(aligned)
 return raw,np.array(arr),start

def make_trace(y,start,name,channel):
 return Trace(data=np.asarray(y,dtype=np.float32),header={'network':'AM','station':name,'location':'00','channel':channel,'starttime':start,'sampling_rate':FS})

def plot_event(r,x,mv,ds,times,fit,snr,output,fit_start,fit_end,flags):
 fig=plt.figure(figsize=(14,13),layout='constrained');gs=fig.add_gridspec(4,2,height_ratios=[1.55,.9,1.3,1.2],width_ratios=[1,1])
 a=fig.add_subplot(gs[0,:]);colors=plt.get_cmap('tab10').colors
 for i,(label,st,_,_) in enumerate(ST):
  scale=max(np.quantile(abs(x[i]),.995),1);a.plot(times,x[i]/scale*.38+4-i,color=colors[i],lw=.55,label=f'{label} / {st}')
 a.set_yticks(range(5),[f'{ST[4-i][0]} / {ST[4-i][1]}' for i in range(5)]);a.set_ylabel('EHZ, scaled per station');a.set_title('Five original EHZ traces, common time grid | 0.5–10 Hz',loc='left')
 b=fig.add_subplot(gs[1,:],sharex=a);b.plot(times,ds/max(snr['ds_noise'],1e-9),color='.65',lw=.6,label='Delay-sum reference');b.plot(times,mv/max(snr['mv_noise'],1e-9),color='#174d78',lw=.7,label='IAS-directed MVDR');b.set_ylabel('Beam / noise RMS');b.legend(loc='upper right',fontsize=8);b.set_title('Beam time series; fixed direction and fixed MVDR weights',loc='left')
 c=fig.add_subplot(gs[2,:],sharex=a);f,tt,ps=spectrogram(mv,fs=FS,window='hann',nperseg=100,noverlap=90,scaling='density');db=10*np.log10(np.maximum(ps,1e-30)/max(ps.max(),1e-30));im=c.pcolormesh(tt+times[0],f,db,shading='auto',cmap='magma',vmin=-60,vmax=0,rasterized=True);c.set_ylim(.5,10);c.set_ylabel('Frequency (Hz)');c.set_xlabel('Seconds relative to BPPTKG event time');c.set_title('Spectrogram of MVDR beam (relative PSD; uncalibrated counts)',loc='left');fig.colorbar(im,ax=c,label='dB relative to event maximum',pad=.01)
 for ax in [a,b,c]:
  ax.axvline(0,color='#bd4b34',ls='--',lw=.8);ax.axvspan(0,float(r['duration']),color='#d9a944',alpha=.12);ax.set_xlim(times[0],times[-1])
 for ax in [a,b]:ax.grid(alpha=.15)
 d=fig.add_subplot(gs[3,0]);im=d.pcolormesh(fit['axis'],fit['axis'],fit['power_db'].T,shading='auto',cmap='viridis',vmin=-15,vmax=0);d.scatter(fit['sx'],fit['sy'],s=70,marker='*',c='r',edgecolors='white',linewidths=.5);d.set_xlabel('East slowness (s/km)');d.set_ylabel('North slowness (s/km)');d.set_aspect('equal');d.set_title('IAS-Capon power, 1–8 Hz | dl=1',loc='left');fig.colorbar(im,ax=d,label='Relative power (dB)',pad=.02)
 e=fig.add_subplot(gs[3,1]);e.axis('off');baz='undefined' if fit['baz'] is None else f"{fit['baz']:.1f} deg";vel='infinite / unresolved' if fit['velocity'] is None else f"{fit['velocity']:.2f} km/s"
 text=(f"Catalog class: {r['eventtype']} (source not independently confirmed)\nCatalog duration: {float(r['duration']):.2f} s\nIAS fit: {fit_start:.2f} to {fit_end:.2f} s; {fit['snapshots']} snapshots\nBackazimuth: {baz}; apparent velocity: {vel}\nSlowness: E {fit['sx']:.2f}, N {fit['sy']:.2f} s/km\nNoise baseline: -50 to -10 s\nMVDR event-RMS/noise-RMS: {snr['mvdr_event_rms_snr']:.2f}\nDelay-sum event-RMS/noise-RMS: {snr['ds_event_rms_snr']:.2f}\nFlags: {', '.join(flags) if flags else 'none'}\nWGS84 coordinates; no instrument-response removal\nShading = catalog duration; red dashed = catalog time")
 e.text(0,.98,text,va='top',fontsize=9,linespacing=1.6)
 local=UTCDateTime(r['start_utc'])+7*3600
 fig.suptitle(f"{r['eventtype']} | {r['start_utc'][:19]} UTC | {str(local)[:19]} WIB\nUGM EHZ array • IAS-Capon direction estimate + MVDR waveform",fontsize=14)
 fig.savefig(output,dpi=160);plt.close(fig)

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--archive',type=Path,required=True);ap.add_argument('--candidates',type=Path,required=True);ap.add_argument('--qc-metrics',type=Path,required=True);ap.add_argument('--limit',type=int);args=ap.parse_args()
 for sub in ['figures','waveforms','beam_products','metadata']: (OUT/sub).mkdir(exist_ok=True)
 candidates=list(csv.DictReader(open(args.candidates)));metrics={r['source_line']:r for r in map(json.loads,args.qc_metrics.open())}
 if args.limit:candidates=candidates[:args.limit]
 result=[];rejected=[]
 for r in candidates:
  ident=r['source_line'];t=UTCDateTime(r['start_utc']);eventid=f"{t.strftime('%Y%m%dT%H%M%S')}_{r['eventtype']}_row{ident}";peak=metrics[ident]['EHZ']['peak_delay_seconds'];end=max(180.,float(r['duration'])+120,peak+120,float(r.get('cut_end_relative_s') or 0))
  try:
   raw,x,start=load_cut(args.archive,t,end);times=-60+np.arange(x.shape[1])/FS
   fit_start=max(0.,peak-8);fit_end=fit_start+32
   z=x[:,(times>=fit_start)&(times<fit_end)];fit=ias_capon(z,xy)
   sensitivity=[]
   for dl in [10.,100.]:
    zf=ias_capon(z,xy,dl=dl);sensitivity.append({'dl':dl,'baz_deg':zf['baz'],'sx':zf['sx'],'sy':zf['sy']})
   mv,ds=beams(x,xy,fit);noise=(times>=-50)&(times<-10);sig=(times>=0)&(times<=max(float(r['duration']),peak+15));rms=lambda v:float(np.sqrt(np.mean(v*v)))
   snr={'mv_noise':rms(mv[noise]),'ds_noise':rms(ds[noise]),'mvdr_event_rms_snr':rms(mv[sig])/max(rms(mv[noise]),1e-12),'ds_event_rms_snr':rms(ds[sig])/max(rms(ds[noise]),1e-12)}
   flags=[]
   if fit['boundary']:flags.append('slowness-grid-boundary')
   if fit['near_zero_slowness']:flags.append('BAZ-poorly-resolved-near-zero-slowness')
   shifts=[np.hypot(q['sx']-fit['sx'],q['sy']-fit['sy']) for q in sensitivity]
   if max(shifts)>.25:flags.append('diagonal-loading-sensitive')
   if snr['mvdr_event_rms_snr']<2:flags.append('weak-MVDR-event-RMS')
   # Post-event quiet tail is diagnostic, not a source-confirmation filter.
   noiser=np.sqrt(np.mean(x[:,noise]**2,axis=1));env=np.median(np.sqrt(np.maximum(uniform_filter1d(x*x,size=25,axis=1),0))/noiser[:,None],axis=0)
   if np.median(env[times>end-20])>2:flags.append('coda-or-other-signal-remains-at-cut-end')
   raw.write(str(OUT/'waveforms'/f'{eventid}_EHZ_RAW.mseed'),format='MSEED',encoding='STEIM2')
   processed=Stream([make_trace(xx,start,ST[i][1],'EHZ') for i,xx in enumerate(x)]);processed.write(str(OUT/'waveforms'/f'{eventid}_EHZ_25Hz.mseed'),format='MSEED',encoding='FLOAT32')
   Stream([make_trace(mv,start,'MVDR','BHZ'),make_trace(ds,start,'DAS','BHZ')]).write(str(OUT/'beam_products'/f'{eventid}_BEAMS.mseed'),format='MSEED',encoding='FLOAT32')
   np.savez_compressed(OUT/'beam_products'/f'{eventid}_IAS_scan.npz',slowness_axis_s_km=fit['axis'],power_db=fit['power_db'],coordinates_east_north_km=xy)
   metadata={k:v for k,v in r.items()};metadata.update({'event_id':eventid,'clip_start_utc':str(start),'clip_end_utc':str(t+end),'fit_start_relative_s':fit_start,'fit_end_relative_s':fit_end,'sx_s_km':fit['sx'],'sy_s_km':fit['sy'],'backazimuth_deg':fit['baz'],'apparent_velocity_km_s':fit['velocity'],'snapshots':fit['snapshots'],'snr':snr,'loading_sensitivity':sensitivity,'flags':flags,'source_confirmed':False})
   (OUT/'metadata'/f'{eventid}.json').write_text(json.dumps(metadata,indent=2))
   plot_event(r,x,mv,ds,times,fit,snr,OUT/'figures'/f'{eventid}.png',fit_start,fit_end,flags)
   result.append({'event_id':eventid,'source_line':ident,'catalog_type':r['eventtype'],'catalog_start_utc':r['start_utc'],'duration_s':r['duration'],'backazimuth_deg':fit['baz'],'apparent_velocity_km_s':fit['velocity'],'sx_s_km':fit['sx'],'sy_s_km':fit['sy'],'mvdr_event_rms_snr':snr['mvdr_event_rms_snr'],'das_event_rms_snr':snr['ds_event_rms_snr'],'flags':';'.join(flags),'source_confirmed':False})
   print('OK',eventid,'BAZ',fit['baz'],'v',fit['velocity'],'flags',flags,flush=True)
  except Exception as e:rejected.append({'source_line':ident,'start_utc':r['start_utc'],'eventtype':r['eventtype'],'reason':str(e)});print('REJECT',ident,str(e),flush=True)
 with (OUT/'event-summary.csv').open('w') as f:
  if result:w=csv.DictWriter(f,fieldnames=list(result[0]));w.writeheader();w.writerows(result)
 (OUT/'rejected-expanded-windows.json').write_text(json.dumps(rejected,indent=2))
 print('COMPLETE',len(result),'accepted',len(rejected),'rejected',flush=True)
if __name__=='__main__':main()
