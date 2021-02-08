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
choose=int(input("사진은 직접 찍은 사진만 옮기시겠습니까?(예:1/아니요:2):"))
if choose==1:
    from PIL import Image
#install command:pip3 install pillow
for (path, dir, files) in os.walk(sergdir):
    for fn in files:
        c=0
        try:
            pt=os.path.join(path, fn)
            print(pt)
        except UnicodeEncodeError:
            print("unicode error")
        exclist=["$RECYCLE.BIN","Steam","nexon","닌텐도","Temporary",".gif",".asf",".tif",".ra",".ico","wmf","AIX",".GIF",".bmp"]
        for i in exclist:
           if i in pt:
                c=1
                break
        if c==1:
                continue
        tp=str(mimetypes.guess_type(pt)[0])
        print(tp)
        if(os.path.isdir(pt)):
            continue
        tmcp=""
        if "image" in tp:
            if choose==1:
                try:
                    img1=Image.open(pt)
                    meta_data=img1._getexif()
                    info=meta_data[0x9003]
                    print(info)
                except:
                    if 'img1' in locals():
                        img1.close()
                    continue
            tmcp=movdir+"/photo/"+fn
        elif "audio" in tp:
            tmcp=movdir+"/music/"+fn
        elif "video" in tp:
            exclist=["XviD","H.264","720p","1080p"]
            for i in exclist:
                if i in pt:
                    c=1
                    break
            if c==1:
                continue
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