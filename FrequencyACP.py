# Initalize dictionary
test_dict = {"Scott" : 5, "is" : 6, "good" : 5, "at" : 7, "Coding" : 9}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Initalize value
G = 5

# Using Loop
# Selective key values  in dictionary
res = 0
for key in test_dict:
    if test_dict[key] == G:
        res = res+1

# printing result
print("Frequency of G is : " + str(res))