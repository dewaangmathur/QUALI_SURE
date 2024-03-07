def ADD():
    import mysql.connector
    mydb=mysql.connector.connect(user="root",host="localhost",password="tiger",database='AMAZON')
    cursor=mydb.cursor()
    a=input('enter product id: ')
    b=input('enter product name: ')
    c=input('enter product brand: ')
    d=input('enter price: ')
    e=input('enter quantity: ')
    f=input('enter image: ')
    values=(a,b,c,d,e,f)
    run="INSERT INTO AMAZON(PRODUCT_ID,PRODUCT_NAME,PRODUCT_BRAND,PRICE,NUMBER_OF_PRODUCTS,IMAGE) VALUES(%s,%s,%s,%s,%s,%s)"
    cursor.execute(run,values)
    print("Product ADDED SUCCESSFULLY!")
    mydb.commit()
