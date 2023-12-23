import datetime as dt

present_time = dt.datetime.now()
req_time = dt.datetime(2005 , 2 , 6)    #we can use this to acquire info of any date

# use key words in the image of the same file(python tutorials-->modules py-->key words for datetime)
f1 = present_time.strftime('%d-%m-%Y , %A')
print(f'\n{f1}\n')

x = ''
if present_time.strftime('%d') == '31' :
    x = 'st'
elif present_time.strftime('%d') == '03' :
    x = 'rd'
elif present_time.strftime('%d') == '02' :
    x = 'nd'
elif present_time.strftime('%d') == '01' :
    x = 'st'
else:
    x = 'th'


print('___TODAY___')
print(present_time.strftime(f'Date :%d{x} %B %Y \nWeek :%A \nCompiled in-->%I:%M:%S %p'))

y = ''
if req_time.strftime('%d') == '31' :
    y = 'st'
elif req_time.strftime('%d') == '03' :
    y = 'rd'
elif req_time.strftime('%d') == '02' :
    y = 'nd'
elif req_time.strftime('%d') == '01' :
    y = 'st'
else:
    y = 'th'

print(req_time.strftime('___Details of %d-%b-%Y\n___'))
print(req_time.strftime(f'Date :%d{y} %B %Y \nWeek :%A \n'))