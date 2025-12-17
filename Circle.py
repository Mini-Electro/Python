import turtle # importing libary
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
circle = turtle.Turtle() # defined variable

num_sides = 360
side_length = 2
angle = 360.0 / num_sides
#iterate loop for total number of sides
for i in range(num_sides):
    circle.forward(side_length)
    circle.right(angle)

turtle.done()