import turtle
sqaure = turtle.Turtle()
sides = 4
angle = 360

for i in range(sides):
    sqaure.forward(angle)
    sqaure.right(90)

turtle.done()