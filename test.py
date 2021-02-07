import os
import time
import shutil
tardir=input("날짜 별로 분류할 디렉토리를 설정해주세요:")
for (path, dir, files) in os.walk(tardir):
    for fn in files:
        pt=os.path.join(path, fn)
        if(os.path.isdir(pt)):
            continue
        test=time.gmtime(os.path.getmtime(os.path.join(path, fn)))
        os.makedirs(tardir+"/"+str(test.tm_year),exist_ok=True)
        print(fn+"이동중...")
        shutil.move(pt,(tardir+"/"+str(test.tm_year)+"/"+fn))