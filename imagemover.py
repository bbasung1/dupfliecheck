import os
import mimetypes
import shutil
sergdir=input("검색하려는 디렉토리의 이름은?:")
movdir=input("중복값을 옮기려는 디렉토리의 이름은?:")
if not os.path.exists(movdir):
    os.mkdir(movdir)
for (path, dir, files) in os.walk(sergdir):
    for fn in files:
        pt=os.path.join(path, fn)
        print(pt)
        tp=str(mimetypes.guess_type(pt)[0])
        if(os.path.isdir(pt)):
            continue
        if "image" in tp:
            #shutil.cpoy2(pt,movdir+fn)
