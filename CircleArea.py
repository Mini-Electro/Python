def area(radius):
    ar = 3.14 * radius * radius
    print("area of circle is", ar)

def circumference(radius):
    cir = 2 * 3.14 * radius
    print("The circumference is:", cir)


r = int(input("Enter radius of a circle: "))

area(r)

circumference(r)