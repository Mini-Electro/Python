char = input("Enter a character: ")

if len(char) == 1:
    print("The ASCII value of", char, "is", ord(char))
else:
    print("Please enter only a single character!")