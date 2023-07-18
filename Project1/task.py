def my_func(*args):
    if str(args[0]) == None:
        print('not available value')
    else:
        print('value available')
    if int(args[1]) == None:
        print("value not available")
    else:
        print("value available")
    if (args[2])== None:
        print("not available")
    else:
        print("available")
        if int(args[3])==None:
            print("value not available")
        else:
            print("not available")

my_func('hari',18,None,89)