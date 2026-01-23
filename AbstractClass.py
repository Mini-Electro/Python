from abc import ABC, abstractmethod


# create base class
class AbsClass(ABC):

    # Function to print a value
    def print(self, x):
        print("Passed Value:", x)
    
    # Abstract Method
    @abstractmethod
    def task(self):
        print("We are inside the absclass task")

# Create sub class
class test_class(AbsClass):
    def task(self):
        print("We are inside the test_class task")

# object of test_class created
test_obj = test_class()
test_obj.task()
test_obj.print(100)