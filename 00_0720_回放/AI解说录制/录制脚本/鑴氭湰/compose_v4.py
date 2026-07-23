import json, subprocess, os
from PIL import Image, ImageDraw, ImageFont
SCR="/private/tmp/claude-501/-Users-lunayuan------Unity-Project-My-project/45d41eac-2071-4e7c-87d5-22d0c17f1395/scratchpad"
cues=json.load(open(f"{SCR}/rec/voice_cues_full.json"))["cues"]
AUDIO_DUR=382.63; INTRO=10.5; GAME_TARGET=AUDIO_DUR-INTRO
SRC_USE=410.0; FSPTS=round(GAME_TARGET/SRC_USE,4)
W=3840; BARH=320; AVW=340
SUBS=f"{SCR}/subs_v4"; os.makedirs(SUBS,exist_ok=True)
for x in os.listdir(SUBS): os.remove(os.path.join(SUBS,x))
FONT="/System/Library/AssetsV2/com_apple_MobileAsset_Font8/86ba2c91f017a3749571a82f2c6d890ac7ffb2fb.asset/AssetData/PingFang.ttc"
font=ImageFont.truetype(FONT,90,index=0); MAXC=34
def wrap(t):
    o=[]
    while len(t)>MAXC: o.append(t[:MAXC]); t=t[MAXC:]
    o.append(t); return o[:2]
meta=[]
for i,c in enumerate(cues):
    im=Image.new("RGBA",(W,BARH),(0,0,0,0)); d=ImageDraw.Draw(im)
    lines=wrap(c["text"]); lh=104; tot=len(lines)*lh; y0=(BARH-tot)//2
    cx=AVW+(W-AVW)//2
    for j,ln in enumerate(lines):
        bb=d.textbbox((0,0),ln,font=font,stroke_width=5); w=bb[2]-bb[0]
        d.text((cx-w//2,y0+j*lh),ln,font=font,fill=(255,255,255,255),stroke_width=5,stroke_fill=(0,0,0,255))
    fn=f"{SUBS}/c_{i:03d}.png"; im.save(fn); meta.append({"s":c["s"],"e":c["e"],"png":fn})
print(f"{len(meta)} 4K subs @bar{BARH}; FSPTS={FSPTS}", flush=True)
args=["ffmpeg","-y",
 "-t","10.5","-i",f"{SCR}/rec/opening.mp4",
 "-t","410","-i",f"{SCR}/rec/42177_4k.mp4",
 "-stream_loop","-1","-i","/Users/lunayuan/回放/贵妃讲解.mp4",
 "-i","/Users/lunayuan/回放/42177_full.wav",
 "-i",f"{SCR}/rec/gamebgm.wav"]
for m in meta: args+=["-i",m["png"]]
naV=5
fc=[f"[0:v]scale={W}:2020,setsar=1,fps=30,fade=t=out:st=10.0:d=0.5[v0]",
    f"[1:v]trim=0:410,setpts={FSPTS}*PTS,scale={W}:2020,setsar=1,fps=30[v1]",
    "[v0][v1]concat=n=2:v=1[cat]",
    f"[cat]pad={W}:{2020+BARH}:0:0:black[base]",
    "[2:v]crop=720:870:0:0,chromakey=0x1bb636:0.11:0.06,despill=type=green:mix=0.35:expand=0.15,scale=-1:300,fps=30[av]",
    f"[base][av]overlay=25:{2020+(BARH-300)//2}:shortest=0[b0]"]
prev="b0"
for k,m in enumerate(meta):
    fc.append(f"[{prev}][{naV+k}:v]overlay=0:2020:enable='between(t,{m['s']},{m['e']})'[s{k}]"); prev=f"s{k}"
fc.append(f"[4:a]atempo={round(1/FSPTS,4)},adelay=10500|10500,volume=0.22[bgm]")
fc.append("[3:a]volume=1.0[vo]")
fc.append("[vo][bgm]amix=inputs=2:normalize=0:duration=first[aout]")
args+=["-filter_complex",";".join(fc),"-map",f"[{prev}]","-map","[aout]","-t",str(AUDIO_DUR),
       "-c:v","libx264","-preset","veryfast","-crf","22","-pix_fmt","yuv420p",
       "-c:a","aac","-b:a","192k","-movflags","+faststart",f"{SCR}/rec/42177_v4.mp4","-loglevel","error","-stats"]
print("encoding v4 @4K ...",flush=True)
print("rc=",subprocess.run(args).returncode,flush=True)
