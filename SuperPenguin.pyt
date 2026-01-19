# parent class
class Bird:
    def __init__(self):
        print("Bird is ready")
    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim Faster")

# child class
class Penguin(Bird):
    def __init__(self):
        # call super function
        super().__init__()
        print("Penguin is ready")
    
    def whoisThis(self):
        print("Penguin")
    def run(self):
        print("Run Faster")

# Object Creation
peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()