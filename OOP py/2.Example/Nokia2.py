#assigning values outside class for class
class Nokia:
    def __init__(self):
        self.model = 'model'
        self.ram = 'RAM'
        self.rom = 'ROM'
    

    def info(self):
        print('Nokia', self.model , 'Info :')
        print('Model -',self.model)
        print('RAM   -',self.ram)
        print('ROM   -',self.rom , '\n')

print('')

mobile1 = Nokia()
mobile1.model = 'G42'
mobile1.ram = '6GB'
mobile1.rom = '64GB'
mobile1.info()

mobile2 = Nokia()
mobile2.model = 'C32'
mobile2.ram = '8GB'
mobile2.rom = '128GB'
mobile2.info() 