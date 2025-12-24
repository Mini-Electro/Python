try:
    age = int(input("Enter your age: "))
    if age <= 0 and age > 120:
        print("Invaild input.")
    else:
        print("Vaild input!")

    if age%2==0:
        print("Your age is an even number!")
    else:
        print("Your age is an odd number!")

except ValueError:
    print("Wrong value!")