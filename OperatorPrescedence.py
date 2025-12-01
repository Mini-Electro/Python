v = 4
w = 5
x = 8
y = 2
z = 0
z = (v+w) * x / y;
print("Value of (v+w) * x / y is", z)



name = "Alex"
age = 0

if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome.")
else:
    print("Goodbye!")


print("Enter a number (Numerator)")
numn = int(input())
print("Enter a number (Denominator)")
numd = int(input())

if numn%numd==0:
    print("\n" +str(numn)+ " is divisible by " +str(numd))
else:
    print("\n" +str(numn)+ " is not divisible by " +str(numd))