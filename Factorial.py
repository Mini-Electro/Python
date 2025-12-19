def factorial(x):
    """this is a recursive function to find the factorial of an integer"""


    if x == 0 or x == 1:
        return 1
    else:
        #calling function inside a function
        return x*factorial(x-1)
    
#display result
print(factorial.__doc__)

print("the factorial of 5:",factorial(5))