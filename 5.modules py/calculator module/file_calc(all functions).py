import calculator as calc   #Importing a module
                            #giving short name for typing relaxation
x = 10
y = 2

#Using functions in the module
a = calc.add(x,y)
print(a)
s = calc.sub(x,y)
print(s)
m = calc.mul(x,y)
print(m)
d = calc.div(x,y)
print(d)

#printing(accessing) variable in that module

mod_var = calc.v

print(mod_var)