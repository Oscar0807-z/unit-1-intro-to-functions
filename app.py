import turtle
from turtle import *
t = Turtle()




t.shape('turtle')
""" def triangle(x):
    for i in range (3):
        t.forward(125)
        t.left(120)

triangle(200) """
def square (x):
    def addSquares(iRange):
        length = 25
        for i in range(iRange):
            square(5, 90)
        length += 5
addSquares(60)
turtle.done()