import os
from PIL import Image
#install command:pip3 install pillow
import shutil
os.makedirs("E:/gather/notexif",exist_ok=True)
for (path, dir, files) in os.walk("E:/gather/photo"):
    for fn in files:
        pt=os.path.join(path, fn)
        if(os.path.isdir(pt)):
            continue
        try:
            img1=Image.open(pt)
            meta_data=img1._getexif()
            info=meta_data[0x9003]
            print(fn+"보존")
        except:
            if 'img1' in locals():
                img1.close()
            tmcp="E:/gather/notexif/"+fn
            shutil.move(pt,tmcp)
            print(fn+"은 exif가 없습니다.")
            