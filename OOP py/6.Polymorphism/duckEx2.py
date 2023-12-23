class India:
    def captal(self):
        print('\nOur captal city is New delhi\n')


    def language(self):
        print('Our national language is Hindi\n')


class USA:
    def captal(self):
        print('Our captal city is Washington D.C\n')


    def language(self):
        print('Our national language is English\n')


def capLan(obj):    # Single method is used to perform more class commands
    obj.captal()    # same method changing into various forms i.e polymorphing
    obj.language()

x = India()
y = USA()
print('___From class India___')
capLan(x)
print('___From class USA___\n')
capLan(y)   