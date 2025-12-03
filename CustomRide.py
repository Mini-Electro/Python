print("Select your ride:")
print("1. Bike")
print("2. Car")


# take input 1 or 2
# select your ride
choice = int(input("Enter Your Choice: "))

#User entering option 1

if (choice == 1):
    print("What type of bike? ")
    print("1. Scooty\n")
    print("2. Scooter\n")

    #Condition for selecting the type of bike

    choice2 = int(input("Enter your bike choice: "))

    if choice2==1:
        print("you have selected Scooty")
    else:
        print("You have selected Scooter")


elif (choice == 2):
    print("What type of car?")
    print("1. Sedan\n")
    print("2. XUV\n")
    choice3 = int(input("Enter your Car Choice: "))

    if choice3 == 1:
        print("You have selected Sedan.")
    else:
        print("You have selected the XUV.")
else:
    print("Wrong Choice!")