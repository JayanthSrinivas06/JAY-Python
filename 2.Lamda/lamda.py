add = lambda a,b : a+b
multi = lambda a,b : a*b
div = lambda a,b : a/b
sub = lambda a,b : a-b

e = '1'

while e != '0':
    a = float(input('Enter 1st number= '))
    b = float(input('Enter 2st number= '))
    op = input('Operation(+ or - or * or /)=')
    if op == '+':
        r1 = add(a,b)
        print(a , op , b , '=' , r1)
    elif op == '*':
        r2 = multi(a,b)
        print(a , op , b , '=' , r2)
    elif op == '/':
        r3 = div(a,b)
        print(a , op , b , '=' , r3)
    elif op == '-':
        r4 = sub(a,b)
        print(a , op , b , '=' , r4)    
    else:
        print('Please enter either + or * or / or -')
    e = input('press any key to continue or 0 to exit.....')  