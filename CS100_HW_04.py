'''
Navado Wray
CS 100 18S Section 004
HW 04, February 1, 2018
'''
import turtle #Imports turtle
a=3
b=4
c=5
if a<b:
    print('OK')
if c<b:
    print('OK')
if a+b==c:
    print('OK')
if a**2+b**2==c**2:
    print('OK')
else:
    print('NOT OK')
t=turtle.Turtle()
def line():                                 #Defines line function
        t.forward(length)
def triangle():                             #Defines triangle function
    n=3
    angle=360/n
    for e in range(n):
        t.forward(length)
        t.left(angle)
def square():                               #Defines square function
    n=4
    angle=360/n
    for e in range(n):
        t.forward(length)
        t.left(angle)
length=int(input('How far?'))               #User tells turtle how far to go
width=input('How wide?')                    #User defines width of turtle
t.width(width)
color=input('What color?')                  #User defines color of turtle
t.color(color)
shape=input('Line, triangle, square')       #Tells turtle what shape to make

if shape==('triangle'):                     #If user enters a triangle, the pre-defined triangle function runs
    triangle()
elif shape==('square'):                     #If user enters a square, the pre-defined square function will run
    square()
elif shape==('line'):                       #If user enters a line, the pre-defined line function will run
    line()
else:
    print ('Error:Shape entered not supported') 
