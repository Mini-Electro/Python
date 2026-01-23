class BMW():
    def mileage(self):
        print("BMW goes on for 46.87 MPG")
    
    def speed(self):
        print("BMW speed is 190 MPH.")
    
    def cost(self):
        print("BWM costs $34,000")

class Ferrari():
    def mileage(self):
        print("Ferrari goes on for 8.77 kmpl")

    def speed(self):
        print("Ferrari speed is 340 km/h.")

    def cost(self):
        print("Ferrari costs $100,000")

# Object Creation
obj_BMW = BMW()
obj_Ferrari = Ferrari()


# Common interface
for car in (obj_BMW, obj_Ferrari):
    car.mileage()
    car.speed()
    car.cost()