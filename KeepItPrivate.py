# class creation

class MyClass:

    # private variable
    __privateVar = 27;

    # private method
    def __privMeth(self):
        print("I'm inside class myClass")

    # function to print value of private variable
    def hello(self):
        print("Private variable value:", MyClass.__privateVar)


foo = MyClass()
foo.hello()
foo.__privMeth()