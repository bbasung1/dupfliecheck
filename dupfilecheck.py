import os
import hashlib
import timeit
name=[]
md=[]
strarttime=timeit.default_timer()
k = open("log.txt", "w")
choose=int(input("같은 파일인지 분석만 하시겠습니까?파일 크기까지 맞을 시 삭제하시겠습니까?(1/2):"))
for (path, dir, files) in os.walk("./"):
    for fn in files:
        pt=os.path.join(path, fn)
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
            print("분석 완료")
            continue
        k.write(pt+"와"+name[md.index(md5)]+"가 같은 파일인거 같습니다. md5="+md5+"\n")
        if choose==2:
            if(os.path.getsize(name[md.index(md5)])==os.path.getsize(pt)):
                os.remove(pt)
        print("분석 완료")
k.close()
endtime=timeit.default_timer()
print("%f"%(endtime - strarttime))