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
        tp=str(mimetypes.guess_type(pt)[0])
        print(tp)
        if(os.path.isdir(pt)):
            continue
        if "image" in tp:
            shutil.copy2(pt,movdir+"/photo/"+fn)
        elif "audio" in tp:
            shutil.copy2(pt,movdir+"/music/"+fn)
        elif "video" in tp:
            shutil.copy2(pt,movdir+"/movie/"+fn)
#audio,video