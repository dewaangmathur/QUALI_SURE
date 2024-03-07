def ADMINCHECK():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="tiger",database='INNOHACK')
    c=mydb.cursor()
    c.execute('select * from ADMINCHECK')
    x=c.fetchall()
    global g
    g=False
    a=input('enter username')
    b=input('enter password(caps lock sensitive):')
    for i in x:
        if i[0]==a and i[1]==b:
            g=True
    if g==False:
        print('access denied')
    else:
        print('logging in to admin \
.\
.\
.\
.\
.\
.\
.\
.\
.\
.\
.\
.\
.')
        import ADMIN_INTERFACE_TO_DELETE,ADD,SHOW,UPDATE_INNOHACK
        ADMIN_INTERFACE_TO_DELETE,ADD,SHOW,UPDATE_INNOHACK.ADMIN()

