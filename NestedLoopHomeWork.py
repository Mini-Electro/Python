decimal = float(input("Enter a decimal number: "))
binary = ""

temp = decimal
while temp > 0:
    binary = str(temp%2) + binary
    temp //= 2

print("Binary Number:", binary)