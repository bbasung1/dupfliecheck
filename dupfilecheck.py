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
        t.write("\ncurrent a1:"+str(a)+"\n")
        t.write("\ncurrent i1:"+str(i)+"\n")
        t.write("\ncurrent k1:"+str(k)+"\n")
        t.write("\ncurrent r1:"+str(md.index(name))+"\n")
        if(a == name):
            t.write("\ncurrent a2:"+str(a)+"\n")
            t.write("\ncurrent i2:"+str(i)+"\n")
            f.write(nm[0]+"와"+nm[md.index(name)]+"가 같은 파일인것 같습니다. MD5="+md[md.index(name)]+"\n")
            #t.write("\ncurrent delposition:"+'\n'.join([str(i+k)]))
            #t.write("\ncheck nmdel:"+"\n".join(nm))
            #t.write("\ncheck mddel:"+"\n".join(md))
        k+=1
t.write("\nfinal nml:"+"\n".join(nm))
t.write("\nfinal md:"+"\n".join(md))
t.close()
f.close()
