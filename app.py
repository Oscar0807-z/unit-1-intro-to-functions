import turtle
from turtle import *
t = Turtle()



t.shape('turtle')
def square (x):
    for i in range(4):
        t.forward (100)
        t.left (90)

def addSquares(60):
    length = 5
    for i in range(iRange):
        square(length)
        length += 25
addSquares(5)
turtle.done()