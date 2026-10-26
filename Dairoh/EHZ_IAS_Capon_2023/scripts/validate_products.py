import json,csv,hashlib,platform,re
from pathlib import Path
import numpy as np,scipy,matplotlib,obspy
from obspy import read,UTCDateTime
from PIL import Image
P=Path(__file__).resolve().parents[1];a=list(csv.DictReader((P/'event-summary.csv').open()));assert len(a)==40
checks=[]
for r in a:
 ident=r['event_id'];m=json.loads((P/'metadata'/f'{ident}.json').read_text());expected=round((UTCDateTime(m['clip_end_utc'])-UTCDateTime(m['clip_start_utc']))*25)+1
 raw=read(str(P/'waveforms'/f'{ident}_EHZ_RAW.mseed'));processed=read(str(P/'waveforms'/f'{ident}_EHZ_25Hz.mseed'));beam=read(str(P/'beam_products'/f'{ident}_BEAMS.mseed'))
 assert len(raw)==5 and len(processed)==5 and len(beam)==2,ident
 assert all(t.stats.channel=='EHZ' and t.stats.sampling_rate==100 for t in raw),ident
 assert all(t.stats.npts==expected and t.stats.sampling_rate==25 and np.isfinite(t.data).all() for t in list(processed)+list(beam)),ident
 assert not processed.get_gaps() and not beam.get_gaps(),ident
 with Image.open(P/'figures'/f'{ident}.png') as im:im.verify()
 scan=np.load(P/'beam_products'/f'{ident}_IAS_scan.npz');assert scan['power_db'].shape==(121,121) and np.isfinite(scan['power_db']).all(),ident
 checks.append({'event_id':ident,'raw_stations':len(raw),'processed_samples_per_station':expected,'status':'PASS'})
badlinks=[]
for f in P.glob('*.md'):
 for target in re.findall(r'\]\(([^)]+)\)',f.read_text()):
  if target.startswith(('http:','https:','#','mailto:')):continue
  if not (f.parent/target.split('#')[0]).exists():badlinks.append([str(f.name),target])
# These files are produced by this validator itself.
badlinks=[x for x in badlinks if x[1] not in ['artifact-validation.json','SHA256SUMS.txt']]
assert not badlinks,badlinks
s={'events_checked':40,'raw_mseed_files':40,'processed_mseed_files':40,'beam_mseed_files':40,'scan_npz_files':40,'pngs_verified':40,'metadata_files':40,'relative_markdown_links':'PASS','all_products_status':'PASS','checks':checks}
(P/'artifact-validation.json').write_text(json.dumps(s,indent=2));(P/'metadata/environment.json').write_text(json.dumps({'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'obspy':obspy.__version__,'matplotlib':matplotlib.__version__},indent=2))
files=sorted(f for f in P.rglob('*') if f.is_file() and '__pycache__' not in f.parts and f.name!='SHA256SUMS.txt' and f.suffix!='.pyc');(P/'SHA256SUMS.txt').write_text(''.join(hashlib.sha256(f.read_bytes()).hexdigest()+'  '+f.relative_to(P).as_posix()+'\n' for f in files))
print(json.dumps({k:v for k,v in s.items() if k!='checks'},indent=2))
