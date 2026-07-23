import sys, time, importlib.util
import numpy as np
from PIL import Image
SCR="/private/tmp/claude-501/-Users-lunayuan------Unity-Project-My-project/45d41eac-2071-4e7c-87d5-22d0c17f1395/scratchpad"
spec=importlib.util.spec_from_file_location("cdp",SCR+"/cdp.py"); cdp=importlib.util.module_from_spec(spec); spec.loader.exec_module(cdp)
MAXDUR=780.0; GO="LYCHEE_REPLAY_DEMO"
ws,url=cdp.page_ws("litchi"); c=cdp.CDP(ws); c.cmd("Page.enable"); c.cmd("Runtime.enable")
def sm(m,a): return c.eval("window.__unityInstance.SendMessage('%s','%s','%s'); 'ok'"%(GO,m,a))
def log(x): print("[v6rec] "+x, flush=True)
def goldfrac(path):
    a=np.asarray(Image.open(path).convert("RGB")).astype(int); R,G,B=a[:,:,0],a[:,:,1],a[:,:,2]
    m=(R>140)&(G>110)&(B<130)&(R>B+35); return float(m.mean())
sm("SetPlayingWeb","false"); sm("SeekToRoundWeb","5"); sm("SetPlayingWeb","false")
time.sleep(1); sm("SetPlayingWeb","false"); time.sleep(0.5)
c.screenshot(SCR+"/rec/v6_start.png"); log("clean start R5 @4K gf=%.2f"%goldfrac(SCR+"/rec/v6_start.png"))
CAP=('(function(){var c=document.getElementById("unity-canvas");var vs=c.captureStream(30);'
 'var vt=vs.getVideoTracks()[0];var at=window.__gameAudioStream.getAudioTracks()[0];'
 'var cs=new MediaStream([vt,at]);'
 'var rec=new MediaRecorder(cs,{mimeType:"video/mp4;codecs=avc1.640028,mp4a.40.2",videoBitsPerSecond:20000000,audioBitsPerSecond:128000});'
 'var chunks=[];rec.ondataavailable=function(e){if(e.data&&e.data.size)chunks.push(e.data);};'
 'window.__rec={rec:rec,chunks:chunks,st:function(){return{n:chunks.length,state:rec.state};}};'
 'rec.start();return "started single-blob";})()')
log("capture -> "+str(c.eval(CAP)))
t0=time.time(); sm("SetPlayingWeb","true"); log("PLAY. record until settlement (cap %ds)"%int(MAXDUR))
lowcnt=0; settled=False; nxt=30
while time.time()-t0 < MAXDUR:
    time.sleep(6); el=time.time()-t0
    if el>=nxt:
        try:
            p=SCR+("/rec/v6p_%03d.png"%int(el)); c.screenshot(p); gf=goldfrac(p)
            log("t=%ds gf=%.2f"%(int(el),gf))
            if el>240 and gf<0.13:
                lowcnt+=1
                if lowcnt>=2 and not settled:
                    settled=True; log("SETTLEMENT detected at t=%ds; holding 14s"%int(el)); time.sleep(14); break
            else: lowcnt=0
        except Exception as e: log("moniterr %s"%str(e)[:50])
        nxt+=30
sm("SetPlayingWeb","false")
fin=c.eval("(async()=>{var R=window.__rec;R.rec.stop();await new Promise(function(r){R.rec.onstop=r;});var b=new Blob(R.chunks,{type:'video/mp4'});var r=await fetch('http://127.0.0.1:8091/upload?name=42177_4k_raw.mp4&reset=1',{method:'POST',body:b});return JSON.stringify({size:b.size,ok:r.ok,n:R.chunks.length});})()", awaitp=True)
c.screenshot(SCR+"/rec/v6_end.png"); log("STOPPED settled=%s %s elapsed=%.1f"%(settled,str(fin),time.time()-t0))
