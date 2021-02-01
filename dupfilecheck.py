import os
import hashlib
nm = []
md = []
k = open("log.txt", "w")
for (path, dir, files) in os.walk("./"):
    for fn in files:
        if(os.path.isdir(os.path.join(path, fn))):
            continue
        f = open(os.path.join(path, fn), "rb")
        data = f.read()
        md5=(hashlib.md5(data).hexdigest())
        print(os.path.join(path, fn))
        print(md5)
        #nm.append(os.path.join(path, fn))
        co=0
        for i in md:
            if(i==md5):
                print(i)
                ind=md.index(i)
                k.write(os.path.join(path, fn)+"와"+nm[ind]+"가 같은 파일인것 같습니다. md5="+md5+"\n")
                co+=1
        if(co==0):
            nm.append(os.path.join(path, fn))
            md.append(md5)
            print(nm)
            print(md)
k.close()