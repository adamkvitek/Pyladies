from turtle import forward, left, right, exitonclick, shape
from math import sqrt

shape('turtle')

for i in range(6):
    for j in range(4):
        forward(100)
        left(90)
    left(45)
    forward(100 * sqrt(2))
    left(90)
    forward(100 * sqrt(2) / 2)
    left(90)
    forward(100 * sqrt(2) / 2)
    left(90)
    forward(100 * sqrt(2))
    left(45)
    forward(10)

