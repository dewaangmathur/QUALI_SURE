def MAIN():
    while True:
        z=input('enter your choice')
        if z=='1':
            import ADMIN_INTERFACE_TO_DELETE,ADD,SHOW,UPDATE_INNOHACK
            ADMIN_INTERFACE_TO_DELETE,ADD,SHOW,UPDATE_INNOHACK.ADMIN()
        elif z=='2':
           import SHOW_INNOHACK_TABLE
           SHOW_INNOHACK_TABLE.SHOW()
        elif z=='3':
           print('thank you for visiting')
           break
        else:
            print('INVALID')
            break
