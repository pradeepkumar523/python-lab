n = input('enter the year')
if n%4 == 0:
    if n%100 == 0:
        if n%400 == 0:
           print('(n) is leap year' ,format(n))
        else:
           print('(n) is leap year' ,format(n))
    else:
        print('(n) is not leap year' ,format(n))
else:
    print('( n) is not leap year' ,format(n)) 
