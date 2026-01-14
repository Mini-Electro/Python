# create class
class Vehicle:


    #create init
    def __init__(self, max_speed, mileage):


        # bind the arguments
        self.maxspeed = max_speed
        self.mileage = mileage


# Object Creation
modelX = Vehicle(240,18)


# access the variables inside init method

print("Model Max Speed:", modelX.maxspeed)
print("Model Mileage:", modelX.mileage)