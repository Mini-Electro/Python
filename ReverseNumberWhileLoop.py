num = int(input("Enter your number: "))

rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num//10

print("Reversed Number is:", rev)