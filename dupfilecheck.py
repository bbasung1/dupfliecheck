import os
import hashlib
import sqlite3
if os.path.exists('temp.db'):
    os.remove('temp.db')
con=sqlite3.connect('temp.db')
cur=con.cursor()
cur.execute("create table temp(name text,md5 text)")
k = open("log.txt", "w")
for (path, dir, files) in os.walk("./"):
    for fn in files:
        pt=os.path.join(path, fn)
        if(os.path.isdir(pt)):
            continue
        f = open(pt, "rb")
        data = f.read()
        md5=(hashlib.md5(data).hexdigest())
        print(pt)
        print(md5)
        #nm.append(os.path.join(path, fn))
        cur.execute("insert into temp values('"+pt+"','"+md5+"')")
        con.commit()
        cur.execute("select * from temp where md5='"+md5+"'")
        while(True):
            row=cur.fetchone()
            if row==None:
                break
            data1=row[0]
            data2=row[1]
            if(data1==pt and data2==md5):
                continue
            k.write(pt+"와"+data1+"가 같은 파일인거 같습니다. md5="+data2+"\n")
            print("here")
k.close()
con.close()