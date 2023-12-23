class Intro:
    x = 99
    def samplemethod(myObject):     #we can use anything instead of self,but 'self' is more convenient and mandatory
        print('value:',myObject.x)


obj1 = Intro()

obj1.samplemethod()
Intro.samplemethod(obj1) 