# parent class
class Person(object):
    def __init__(self,name,idNumber):
        self.Name = name
        self.IdNumber = idNumber
        
    def display(self):
        print(self.Name)
        print(self.IdNumber)

# child class
class Employee(Person):
    def __init__(self, name, idNumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idNumber)


a = Employee("Rahul", 886012, 200000, "Intern")

a.display() 