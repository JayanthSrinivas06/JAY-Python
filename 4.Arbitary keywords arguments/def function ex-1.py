def person(**data):  #a variable in function if inserted with'**' as suffix is called Arbitary keyword arguements
    print(data)      #it creates dictionary
    for k,v in data.items():
        print(k, ':', v)    #prints individually

person(fName = 'Jayanth', lName='Srinivas', Age=18, Mobile=123456)    
    