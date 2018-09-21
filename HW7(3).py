'''Navado Wray
CS100 Section 004
March 19,2018
'''
#3
def enterNewPassword():
    while True:
        password=input('Enter Password/nPassword must be 8-15 characters long nad contain at least one digit')
        digits= '0123456789'
        hasDigit = False
        isGoodLength = False
        if len(password)<=15 and len(password)>=8:
            isGoodLength = True
        for char in password:
            if char in digits:
                hasDigit = True
        if hasDigit and isGoodLength:
            break
    
enterNewPassword()
        

