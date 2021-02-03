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
choose=int(input("같은 파일인지 분석만 하시겠습니까?파일 크기까지 맞을 시 삭제하시겠습니까?(1/2):"))
count=0
for (path, dir, files) in os.walk(sergdir):
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
            #print(os.path.basename(pt))
            print("분석 완료")
            continue
        k.write(pt+"와"+name[md.index(md5)]+"가 같은 파일인거 같습니다. md5="+md5+"\n")
        #print(os.path.basename(pt))
        if choose==2:
            if os.path.basename(name[md.index(md5)])!=os.path.basename(pt):
                 s=os.path.splitext(pt)
                 wa=s[0]
                 wa+="v"
                 tmcp=wa+s[1]
                 os.rename(pt,tmcp)
                 pt=tmcp
            s=os.path.basename(pt)
            tmcp=movdir+"/tmp/"+s
            ct=0
            if os.path.exists(tmcp):
                s=os.path.splitext(tmcp)
                wa=s[0]
                while os.path.exists(wa+str(ct)+s[1]):
                    ct+=1
                tmcp=wa+str(ct)+s[1]
            shutil.move(pt,tmcp)
        print("분석 완료")
k.close()
endtime=timeit.default_timer()
print("%f"%(endtime - strarttime))