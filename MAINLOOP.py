def MAIN():
    while True:  
         print("===============================")
         print("")
         print("******WELCOME TO E-COMMERCE******* \n World's best e-commerce platform.")
         print("")
         print("===============================")
         print("1.Admin")
         print("2.User")
         print("3.Quit project")
         print("")
         z=input('enter your choice')
         if z=='1':
             import ADMIN_CHECK
             ADMIN_CHECK.ADMINCHECK()
         elif z=='2':
             import SHOW_INNOHACK_TABLE
             SHOW_INNOHACK_TABLE.SHOW()
             c=input('do you want to reserve a product y/n (choice case sensitive)')
             if c=='y':
                 import ADDING_ITEM_IN_TABLE_INNOHACK
                 ADDING_ITEM_IN_TABLE_INNOHACK.ADDORDER()
         elif z=='3':
             print('thank you for visiting')
             break
         else:
             print('INVALID')
             break
