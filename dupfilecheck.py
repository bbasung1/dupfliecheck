import os
import hashlib
import timeit
import shutil
name=[]
md=[]
strarttime=timeit.default_timer()
k = open("log.txt", "w")
sergdir=input("검색하려는 디렉토리의 이름은?:")
movdir=input("중복값을 옮기려는 디렉토리의 이름은?:")
os.makedirs(movdir+"/tmp",exist_ok=True)
choose=int(input("같은 파일인지 분석만 하시겠습니까?파일 크기까지 맞을 시 tmp 폴더로 이동시키겠습니까?(1/2):"))
count=0
for (path, dir, files) in os.walk(sergdir):
    for fn in files:
        pt=os.path.join(path, fn)
        if "tmp" in pt:
            break
        if(os.path.isdir(pt)):
            continue
        print(pt+"분석중....")
        with open(pt, "rb") as f:
            data=hashlib.md5()
            while test := f.read(8192):
                data.update(test)
        md5=data.hexdigest()
        f.close()
        print(md5)
        if md.count(md5)==0:
            md.append(md5)
            name.append(pt)
            #print(os.path.basename(pt))
            print("분석 완료")
            continue
        k.write(pt+"와"+name[md.index(md5)]+"가 같은 파일인거 같습니다. md5="+md5+"\n")
        #print(os.path.basename(pt))
        if choose==2:
            tmcp=movdir+"/tmp/"+os.path.basename(pt)
            shutil.move(pt,tmcp)
        print("분석 완료")
k.close()
endtime=timeit.default_timer()
print("%f"%(endtime - strarttime))