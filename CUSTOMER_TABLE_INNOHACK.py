import mysql.connector
db=mysql.connector.connect(host='localhost',user='root',passwd='tiger',database='AMAZON')
c=db.cursor()
c.execute('CREATE TABLE CUSTOMER(NAME VARCHAR(50) NOT NULL,PRODUCT VARCHAR(50) NOT NULL,QUANTITY CHAR(5) NOT NULL,PHONE_NUMBER INT(10) PRIMARY KEY')


