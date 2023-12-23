x = 99

def example1():
    x = 999         #Consideres x value within the def function only
    print('in func:', x)

example1()
print('1st outside:',x)

print("_____After using 'global'_____")

def example2():
    global x        #Eventhough x value assigned outside if 'global' used it consideres value of this everywhere
    x = 999
    y = 333
    print('in func:', x)
    print('in func:', y)

example2()
print('outside after global:', x)
print(globals()['x'])       #Can access global variables by this keyword
print('outside y :',y)      #Cant access value of y outside the function