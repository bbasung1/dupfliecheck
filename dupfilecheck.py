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
for a in md:
    k = []
    for i, name in enumerate(md):
        if(a == name):
            k.append(i)
    for i in k:
        if i ==0:
            continue
        f.write(nm[0]+"와"+nm[i]+"가 같은 파일인것 같습니다. MD5="+md[i]+"\n")
    for i in k:
        del(nm[i])
        del(md[i])
        t.write(" ".join(nm))
        t.write(" ".join(md))
t.write(" ".join(nm))
t.write(" ".join(md))
t.close()
f.close()
