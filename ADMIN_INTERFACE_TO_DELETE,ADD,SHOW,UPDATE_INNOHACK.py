def ADMIN():
    import ADDING_ITEM_IN_TABLE_INNOHACK
    import UPDATE_INNOHACK_TABLE
    import DELETE_ITEM_FROM_TABLE_INNOHACK
    import SHOW_INNOHACK_TABLE
    x=True
    while x==True:
        print()
        print('1.ADD ORDER')
        print('2.UPDATE ORDER')
        print('3.DELETE ORDER')
        print('4.SHOW ALL ORDERS')
        print('5. EXIT')
        print()
        y=input('ENTER YOUR CHOICE.:')
        print()
        if y=='1':
            ADDING_ITEM_IN_TABLE.ADD()
        elif y=='2':
            UPDATE_INNOHACK_TABLE.UPDATE()
        elif y=='3':
            DELETE_FROM_TABLE_INNOHACK.DELETE()
        elif y=='4':
            SHOW_INNOHACK_TABLE.SHOW()
        elif y=='5':
            print('Thank You')
            break
        else:
            print('wrong CHOICE')


