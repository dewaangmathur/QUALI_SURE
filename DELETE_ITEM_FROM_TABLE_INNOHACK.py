def DELETE():
    import mysql.connector
    mydb=mysql.connector.connect(user="root",host="localhost",password="tiger",database='AMAZON')
    cursor=mydb.cursor()
    a=input('enter PRODUCT ID to be deleted:')
    cursor.execute("delete from AMAZON where PRODUCT_ID='{}'".format(a))
    print("ORDER DELETED SUCCESSFULLY!")
    mydb.commit()
