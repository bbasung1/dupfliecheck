import os
import time
import shutil
from PIL import Image
#install command:pip3 install pillow
tardir=input("날짜 별로 분류할 디렉토리를 설정해주세요:")
for (path, dir, files) in os.walk(tardir):
    for fn in files:
        pt=os.path.join(path, fn)
        if(os.path.isdir(pt)):
            continue
        try:
            img1=Image.open(pt)
            meta_data=img1._getexif()
            info=meta_data[0x9003]
            c=info[0:4]
            img1.close()
            #print(c)
            print("exif에 따라...")
        except:
            if 'img1' in locals():
                img1.close()
            test=time.gmtime(os.path.getmtime(os.path.join(path, fn)))
            c=test.tm_year
            print("옮긴 연도에 따라....")
        os.makedirs(tardir+"/"+str(c),exist_ok=True)
        print(pt+"이동중...")
        shutil.move(pt,(tardir+"/"+str(c)+"/"+fn))
        print("이동 완료")
        #except:
        #    print("이동 중단")
        #    continue
            