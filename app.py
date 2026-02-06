import turtle
from turtle import *
t = Turtle()



t.shape('turtle')
def square (x):
    for i in range(4):
        t.forward (x)
        t.left (90)

def addSquares (iRange):
    length = 25
    for i in range(iRange):
        square(length)
        length += 5
        t.right (5)
addSquares(60)
turtle.done()