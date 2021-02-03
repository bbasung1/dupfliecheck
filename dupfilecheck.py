import os
import hashlib
import sqlite3
import timeit
strarttime=timeit.default_timer()
dbdir=""
if os.name=='nt':
    if not os.path.exists("C:/tmp"):
        os.mkdir("C:/tmp")
    dbdir="c:/tmp/tmpdb"
elif os.name=='posix':
    dbdir="/tmp/temp.db"
if os.path.exists(dbdir):
    os.remove(dbdir)
con=sqlite3.connect(dbdir)
cur=con.cursor()
cur.execute("create table temp(name text,md5 text)")
k = open("log.txt", "w")
choose=int(input("같은 파일인지 분석만 하시겠습니까?파일 크기까지 맞을 시 삭제하시겠습니까?(1/2):"))
for (path, dir, files) in os.walk("./"):
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
        cur.execute("select * from temp where md5='"+md5+"'")
        row=cur.fetchone()
        if row==None:
            cur.execute("insert into temp values(\""+pt+"\",'"+md5+"')")
            con.commit()
            print("분석 완료")
            continue
        data1=row[0]
        data2=row[1]
        k.write(pt+"와"+data1+"가 같은 파일인거 같습니다. md5="+data2+"\n")
        if choose==2:
            cur.execute("select * from temp where rowid in(select min(rowid) from temp where md5=\""+md5+"\")")
            row=cur.fetchone()
            suvname=str(row[0])
            print(suvname)
            if(os.path.getsize(suvname)==os.path.getsize(pt)):
                os.remove(pt)
        cur.execute("delete from temp where rowid not in(select min(rowid) from temp group by md5)")
        con.commit()
        print("분석 완료")
k.close()
con.close()
endtime=timeit.default_timer()
print("%f"%(endtime - strarttime))