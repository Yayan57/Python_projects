password = 'adkl;f'
isPswrd = False
i = 0

while isPswrd == False:
    userinput = input('what is the password:')
    if i < 2:
        if userinput == password:
            print('Access granted')
            isPswrd = True
            break
        elif userinput != password:
            print('Access denied')
            i += 1

    elif i >= 2:
        print('password failed 3 times\n launching the nukes')
        break
