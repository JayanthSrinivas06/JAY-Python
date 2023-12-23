class Bike:
    #class or static variables
    tyres = 2
    def __init__(self):
        #Instance variable
        self.name = 'Activa'
        self.year = '2021'
        self.mileage = '40KMpL'
print()

bike1 = Bike()
print(bike1.name , bike1.year , bike1.mileage , Bike.tyres , '\n')

bike2 = Bike()      #we can change Instance variable values by object name
bike2.name = 'Unicorn'
bike2.year = '2023'
bike2.mileage = '50KMpL'
print(bike2.name , bike2.year , bike2.mileage , Bike.tyres , '\n')

Bike.tyres = 3      #static or class variable values can be changed by class name

bike3 = Bike()
bike3.name = 'Activa5G'
print(bike3.name , bike3.year , bike3.mileage , Bike.tyres , '\n')

bike4 = Bike()
bike4.tyres = 4     #can't change class variable by using object name
bike3.name = 'Jupiter'
print(bike3.name , bike3.year , bike3.mileage , Bike.tyres , '\n')