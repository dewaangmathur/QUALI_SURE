def SHOW():
    import mysql.connector
    mydb=mysql.connector.connect(user="root",host="localhost",password="tiger",database="AMAZON")
    cursor=mydb.cursor()
    sql="select * from INNOHACK_TABLE;"
    cursor.execute(sql)
    i=cursor.fetchall()
    for PRODUCT_ID,PRODUCT_NAME,PRODUCT_BRAND,PRICE,NUMBER_OF_PRODUCTS in i:
        print("%d \t| '%s' \t| '%s' \t| '%d' \t| '%d'"%(PRODUCT_ID,PRODUCT_NAME,PRODUCT_BRAND,PRICE,NUMBER_OF_PRODUCTS))
            
