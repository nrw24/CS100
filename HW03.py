'''
Navado Wray
CS 100 2018S Section 004
HW 03, January 24, 2018
'''

# 1
import turtle
aScreen=turtle.Screen()
brandon=turtle.Turtle()
brandon.showturtle()
triangle_length=100
angle=120
brandon.up()
brandon.right(90)
brandon.forward(150)
brandon.down()
brandon.forward(triangle_length)
brandon.left(angle)
brandon.forward(triangle_length)
brandon.left(angle)
brandon.forward(triangle_length)
brandon.dot()
brandon.penup()
brandon.forward(60)
brandon.right(60)
brandon.pendown()
square_length=100
angle=90
brandon.forward(square_length)
brandon.left(angle)
brandon.forward(square_length)
brandon.left(angle)
brandon.forward(square_length)
brandon.left(angle)
brandon.forward(square_length)
brandon.dot()
brandon.penup()
brandon.forward(50)
brandon.left(90)
angle=72
pentagon_length=100
brandon.forward(pentagon_length)
brandon.pendown()
brandon.left(angle)
brandon.forward(pentagon_length)
brandon.right(angle)
brandon.forward(pentagon_length)
brandon.right(angle)
brandon.forward(pentagon_length)
brandon.right(angle)
brandon.forward(pentagon_length)
brandon.right(angle)
brandon.forward(pentagon_length)
brandon.dot()
#2
brandon.penup()
brandon.left(75)
brandon.forward(170)
brandon.color('light blue')
brandon.width(10)
brandon.left(90)
brandon.forward(300)
brandon.pendown()
brandon.circle(50)
brandon.penup()
brandon.right(90)
brandon.forward(50)
brandon.left(90)
brandon.pendown()
brandon.circle(100)
brandon.penup()
brandon.right(90)
brandon.forward(50)
brandon.left(90)
brandon.pendown()
brandon.circle(150)
brandon.penup()
brandon.right(90)
brandon.forward(50)
brandon.left(90)
brandon.pendown()
brandon.circle(200)

#3
import math
factorial_=math.factorial(100)
print(factorial_)
log=math.log(1000000,2)
print(log)
denominator=math.gcd(63,49)
print(denominator)



