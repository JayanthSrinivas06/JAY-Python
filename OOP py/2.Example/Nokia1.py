class Nokia:
    def __init__(self , model , ram , rom):
        self.model = model
        self.ram = ram
        self.rom = rom
    

    def info(self):
        print('Model :',self.model)
        print('RAM :',self.ram)
        print('ROM :',self.rom, '\n')


mob1 = Nokia('G42' , '6Gb' , '64Gb')
mob1.info()

mob2 = Nokia('C32' , '8Gb' , '128Gb')
mob2.info()