num = 3

if num > 0:
    print(num, "is a positive number.")



num = -1
if num > 0:
    print(num, "is a positive number.")


actual_cost = float(input("Enter the actual cost here: "))
sale_amount = float(input("Enter the sales amount here: "))

if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("Total Profit = {0}".format(amount))
else:
    print("No profit!")


i = int(input("Enter a number: "))

if (i < 15):
    print("i is smaller than 15")
    print("i'm in if block")
else:
    print("i is greater than 15")
    print("i'm in else block")
print("i'm not in if or else Block")

# Check Number is even or odd

number = int(input("Enter a number: "))
print("Number to be checked...", number)

if number%2==0:
    print("Number is even!")
else:
    print("number is odd!")

# Homework:

temp = int(input("Enter the tempature: "))

if temp > 27:
    print("It is summer!, Very warm.")
else:
    print("It is winter!, Very cold")