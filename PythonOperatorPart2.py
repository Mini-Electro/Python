a = 10
b = -10
c = 0

if a and b and c:
    print("All of the numbers are true!")
else:
    print("Atleast one of them are false")


if a > 0 or b > 0:
    print("Either one of the number is greater than 0")
else:
    print("No Number is greater than zero")

if b > 0 or c > 0:
    print("Either one of the number is greater than zero")
else:
    print("No Number is greater than zero")


a = 10
b = 12
c = 12


print(a != b)
print(b != c)

a = "python"
b = "coding"

if a != b:
    print(a, "and", b, "are different.")


a = 4
b = 5

if (a == 1) != (b == 5):
    print("Hello")




a = int(input("Enter a number: "))

if a%2 != 0 :
    print(a, "is not an even number")
else:
    print(a, "is an even Number!")