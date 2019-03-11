from turtle import *
speed(0)
bgcolor("black")
pencolor('#c9fcff')
left(90)
screensize(2000, 2000)
def square_rot(length, pen):
    if (length < 0):
        return
    else:
        pensize(pen)
        forward(length)
        right(90)
        forward(length)
        right(90)
        forward(length)
        right(90)
        forward(length)
        right(80)
        square_rot(length - 4, 1*pen/1.05)

square_rot(400, 10)
exitonclick()
