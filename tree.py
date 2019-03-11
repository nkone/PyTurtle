from turtle import *
left(90)
speed(0)
bgcolor("black")

screensize(2500,2500)

colors = ['#ff3d3d', '#de3dff', '#3d4dff', '#3d7aff', '#3dc8ff', '#3dfff8', '#3dff7a', '#9aff3d', '#d1ff3d', '#fff83d', '#ffae3d', '#ff6a3d']

def tree(size, depth, pen):
    if depth == 0:
        return
    color = pencolor()
    pencolor(colors[depth % len(colors)])
    pensize(pen)
    fd(size)
    left(15)
    tree(6*size/7, depth - 1, 6*pen/7)
    right(30)
    tree(6*size/7, depth - 1, 6*pen/7)
    left(15)
    fd(-size)
    pencolor(color)
    

tree(200, 12, 35)
exitonclick()
