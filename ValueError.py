#using try and except

try:
    number = int(input("Enter a number: "))
    print("The Number entered is,",number)
#using value error
except ValueError as ex:
    print("Exception:", ex)