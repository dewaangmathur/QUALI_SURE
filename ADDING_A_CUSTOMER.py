def ADDORDER():
    import mysql.connector
    mydb=mysql.connector.connect(user="root",host="localhost",password="tiger",database='AMAZON')
    cursor=mydb.cursor()
    a=input('enter your name: ')
    b=input('enter product name: ')
    c=input('enter product quantity: ')
    d=int(input('enter phone no.: '))
    values=(a,b,c,d)
    run="INSERT INTO CUSTOMER VALUES('%s','%s','%s',%d)"
    cursor.execute('select * from INNOHACK_TABLE')
    x=cursor.fetchall()
    f=0
    for i in x:
        if i[1]==b and int(i[2])>=int(c):
            x=int(i[2])
            y=x-int(c)
            cursor.execute("INSERT INTO CUSTOMER VALUES('%s','%s','%s',%d)"%values)
            cursor.execute('update INNOHACK_TABLE SET NUMBER_OF_PRODUCTS="%s" where PRODUCT_NAME="%s"'%(y,b)) 
            print("Your ORDER has been reserved.You will be contacted for payment")
            f=1
            break
    if f==0:
        print('invalid order')
    mydb.commit()
