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
