# Create Class

class Employee:

    # initalizing
    def __init__(self):
        print("Employee Created")

    # calling destructor
    def __del__(self):
        print("Destructor Called")

def Create_obj():
    print("Making Object..")
    obj = Employee()
    print("function end....")
    return obj

print("Calling obj() function...")
obj = Create_obj()
print("Program end...")  
