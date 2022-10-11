
print()

while True:

    password = input('Please add your password: ')
    print()
    counterL = 0
    counterFullDec = 0
    counterU = 0
    counterLo = 0
    counterD = 0
    
    if len(password) >= 8:
        counterL = 1
    
    if password.isdecimal():
        counterFullDec = 1
        
    for i in password:
        if i == i.upper():
            counterU += 1
        if i == i.lower():
            counterLo += 1
        if i.isdecimal():
            counterD += 1    

    if counterL == 0 or counterFullDec == 1 or counterU == 0 or counterLo == 0 or counterD == 0:
        print('The password should:')
        if counterL == 0:
            print('- be at least 8 characters long')
        if counterFullDec == 1:
            print('- contain at least one uppercase letter')
            print('- contain at least one lowercase letter')
        if counterU == 0:
            print('- contain at least one uppercase letter')
        if counterLo == 0:
            print('- contain at least one lowercase letter')
        if counterD == 0:
            print('- contain at least one numeric character')

    if counterL != 0 and counterFullDec == 0 and counterU != 0 and counterLo != 0 and counterD != 0:
        print('The password is saved.')
        print()
        break