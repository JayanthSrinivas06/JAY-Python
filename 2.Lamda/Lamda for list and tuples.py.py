nums = [2 , 5 , 9 , 7 , 10 , 14 , 15 , 19 , 25 , 100 , 101 , 26]
evensL = list(filter(lambda a: a%2 == 0 , nums))
evensT = tuple(filter(lambda a: a%2 == 0 , nums))

print(evensL)
print(evensT)