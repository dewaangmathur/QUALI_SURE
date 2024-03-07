import mysql.connector
db=mysql.connector.connect(host='localhost',user='root',passwd='tiger',database='INNOHACK')
c=db.cursor()
c.execute('create table ADMINCHECK(USENAME varchar(50) primary key,PASSWORD varchar(50) not null)')
c.execute('insert into ADMINCHECK values("dewaang","admin")')
