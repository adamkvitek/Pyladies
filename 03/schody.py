from turtle import forward, left, right, speed, exitonclick, shape

shape('turtle')

for i in range (6):
    for j in range(1):
        forward(45)
        left(90)
        forward(45)
        right(90)

exitonclick()
