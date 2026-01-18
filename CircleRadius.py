import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Take input from the user
radius = float(input("Enter the radius of the circle: "))

# Create an object of the Circle class
circle = Circle(radius)

# Display results
print("Area of the circle:", circle.area())
print("Perimeter of the circle:", circle.perimeter())
