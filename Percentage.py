maths = int(input("Enter Math marks: "))
coding = int(input("Enter Coding marks: "))
sciene = int(input("Enter Sciene marks: "))
pe = int(input("Enter Phyical Education marks: "))

sum = maths+coding+sciene+pe
print("Marks all together is:", sum)

percentage = (sum/400)*100
print("The Percentage of all the marks together is:", percentage)