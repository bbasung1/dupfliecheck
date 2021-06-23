import os
from PIL import Image
for root,dirs,files in os.walk("/home/kwongibum/사진/hum"):
    for idx,file in enumerate(files):
        fname, ext =os.path.splitext(file)
        if ext in ['.png']:
            im=Image.open("/home/kwongibum/사진/hum/"+file)
            ci=im.crop((0,0,1920,1080))
            ci.save(file)