from turtle import forward, left, right, speed, exitonclick, shape

shape('turtle')

for i in range (6):
    for j in range(6):
        forward(45)
        left(60)
    forward(45)
    right(60)

exitonclick()

