import os
import hashlib
nm = []
md = []
for (path, dir, files) in os.walk("./"):
    for fn in files:
        if(os.path.isdir(os.path.join(path, fn))):
            continue
        f = open(os.path.join(path, fn), "rb")
        data = f.read()
        md.append(hashlib.md5(data).hexdigest())
        nm.append(os.path.join(path, fn))
f = open("log.txt", "w")
t=open("debug.txt","w")
k=1
for a in md:
    for i, name in enumerate(md[k:]):
        if(a == name):
            f.write(nm[0]+"와"+nm[i]+"가 같은 파일인것 같습니다. MD5="+md[i]+"\n")
            t.write("current delposition:"+'\n'.join([str(i)]))
            t.write("check nmdel:"+"\n".join(nm))
            t.write("check mddel:"+"\n".join(md))
        k+=1
t.write("final nml:"+"\n".join(nm))
t.write("final md:"+"\n".join(md))
t.close()
f.close()
