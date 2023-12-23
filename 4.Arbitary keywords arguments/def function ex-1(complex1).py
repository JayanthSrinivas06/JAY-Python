def person(**data): 
    for k,v in data.items():
        if k == 'firstName':
            print(k, ':', v)
        elif k == 'lastName':
            print(k, ' :', v)
        elif k == 'Age':
            print(k, '      :', v)
        else:
            print(k, ' :', v)        

e = 1
while e != '0':
    fName = input('Enter your First name:')
    lName = input('Enter your last name:')
    age = input('Enter your Age:')
    mobile = input('Enter your Mobile Number:')
    print('')
    person(firstName=fName , lastName=lName , Age=age , Mobileno=mobile)
    e = input("Press Enter to continue or input '0' to stop...")
              