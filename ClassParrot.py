class Parrot:
    
    species = "Bird"

    def __init__(self, name, Age):
        self.name = name
        self.age = Age


# instantiate the Parrot Class

blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access to the class attributes
print("Blu is a {}".format(blu.species))
print("Woo is a {}".format(woo.species))

# access the instance attributes
print("{} is {} years old.".format(blu.name, blu.age))
print("{} is {} years old.".format(woo.name, woo.age))