base = float(input("Enter the base number: "))
power = int(input("Enter the power (n): "))

result = 1

# Multiply base "power" number of times

for i in range(power):
    result = result * base

print(f"{base} raised to the power {power} is {result}")