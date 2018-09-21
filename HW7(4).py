'''Navado Wray
CS100 Section 004
March 19,2018
'''
#4
import random
def guessNumber():
    num=random.randrange(50)
    i=0
    while num<50 and num>=0:
        guess=int(input('What number am I thinking of?'))
        if guess!=num:
            print('Nope, try again!')
            i+=1
        elif guess==num:
            print('You got it!')
            print(num)
        if i==5:
            print('Too many guesses!')
            break
guessNumber()
6
