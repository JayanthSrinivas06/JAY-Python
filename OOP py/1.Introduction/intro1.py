class Intro:
    x = 99
    def samplemethod(self):
        print(self.x)


obj1 = Intro()

obj1.samplemethod()     #calling variable in def inside a class
Intro.samplemethod(obj1)     #by using class name