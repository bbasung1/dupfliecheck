import os
import time
for (path, dir, files) in os.walk("/media/kwongibum/extend1.5t/gather/tmp"):
    for fn in files:
        print(time.ctime(os.path.getatime(os.path.join(path, fn))))