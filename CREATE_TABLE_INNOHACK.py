import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="tiger",database="AMAZON")
cursor=mydb.cursor()
y="CREATE TABLE INNOHACK_TABLE(PRODUCT_ID INTEGER NOT NULL PRIMARY KEY,PRODUCT_NAME VARCHAR(50) NOT NULL,PRODUCT_BRAND VARCHAR(50) NOT NULL,PRICE VARCHAR(25) NOT NULL,NUMBER_OF_PRODUCTS INTEGER NOT NULL,IMAGE BLOB)"
cursor.execute(y)

