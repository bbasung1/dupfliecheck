import os
import mimetypes
import shutil
sergdir=input("검색하려는 디렉토리의 이름은?:")
movdir=input("중복값을 옮기려는 디렉토리의 이름은?:")
if not os.path.exists(movdir):
    os.mkdir(movdir)
os.makedirs(movdir+"/photo",exist_ok=True)
os.makedirs(movdir+"/movie",exist_ok=True)
os.makedirs(movdir+"/music",exist_ok=True)
for (path, dir, files) in os.walk(sergdir):
    for fn in files:
        pt=os.path.join(path, fn)
        print(pt)
        if   "$RECYCLE.BIN" in pt:
            continue
        if "Steam" in pt:
            continue
        if "nexon" in pt:
            continue
        tp=str(mimetypes.guess_type(pt)[0])
        print(tp)
        if(os.path.isdir(pt)):
            continue
        tmcp=""
        if "image" in tp:
            tmcp=movdir+"/photo/"+fn
        elif "audio" in tp:
            tmcp=movdir+"/music/"+fn
        elif "video" in tp:
            tmcp=movdir+"/movie/"+fn
        else:
            continue
        ct=0
        if os.path.exists(tmcp):
            s=os.path.splitext(tmcp)
            wa=s[0]
            wa+="ver"
            while os.path.exists(wa+str(ct)+s[1]):
                ct+=1
            tmcp=wa+str(ct)+s[1]
        print(tmcp)
        shutil.copy2(pt,tmcp)
#audio,video