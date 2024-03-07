def UPDATE():
    import mysql.connector
    mydb=mysql.connector.connect(user="root",host="localhost",password="tiger",database='INNOHACK')
    cursor=mydb.cursor()
    a=int(input('enter order id to be updated: '))
    b=input('enter updated PRODUCT_NAME: ')
    c=input('enter updated PRODUCT_BRAND: ')
    d=input('enter updated price: ')
    e=input('enter updated number_of_products: ')
    f=input('enter image: ')
    #values=(b,c,d,e,f,a)
    #run="update INNOHACK_TABLE set PRODUCT_NAME='%s',PRODUCT_BRAND='%s',PRICE='%s',NUMBER_OF_PRODUCTS='%s' where ORDER_ID=%d"
    #cursor.execute(run,values)
    cursor.execute("update INNOHACK_TABLE set PRODUCT_NAME='%s',PRODUCT_BRAND='%s',PRICE='%s',NUMBER_OF_PRODUCTS='%s' where ORDER_ID=%d"%(b,c,d,e,a))
    print("ORDER UPDATED SUCCESSFULLY!")
    mydb.commit()
