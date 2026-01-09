numbers = [1,2,3,4,5,6]


even = [x for x in numbers if x%2==0]
print("List of even numbers are:", even)
odd = [x for x in numbers if x%2!=0]
print("List of odd numbers are", odd)