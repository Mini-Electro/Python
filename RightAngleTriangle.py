# Take Input
print("Half Pyramid Pattern of Stars (*):")
n = int(input("Enter the number of rows: "))

# outer loop to handle number of rows

for i in range(n):
    # inner loop to handle number of columns
    for j in range(i+1):
        #display result
        print("* ", end="")
    print()


# Take Input from user again

rows = int(input("Please enter the total number of Rows: "))

number = 1 # initalise by 1

print("Floyd's Triangle")
# Outer loop  for number of rows 
for i in range(1, rows + 1):
    # inner loop for number of columns
    for j in range(1, i + 1):
        #display result
        print(number, end= " ")
        number = number + 1
    print()