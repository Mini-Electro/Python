class FindSumPairs:
    def __init__(self, data):
        self.Data = data


    def find_positions(self, target_sum):
        n = len(self.Data)

        for i in range(n):
            for j in range(i + 1, n):
                # This is where the error occurs if self.Data is a set
                if self.Data[i] + self.Data[j] == target_sum:
                    print(f"Numbers: {self.Data[i]} + {self.Data[j]} = {target_sum}")
                    print(f"Positions: {i} and {j}")
                    return

        print("No Pairs found with the given sum.")

# Given tuple
# Changed from set {} to tuple ()
numbers = (10,20,30,40,50,60,70)

# Create object of the class
# Renamed obj to obj_instance to avoid potential conflict/confusion if 'obj' was used elsewhere, though not strictly necessary for this specific fix.
obj_instance =  FindSumPairs(numbers)

# Take sum from the user
target = int(input("Enter the sum you want to find: "))

# Call the method
obj_instance.find_positions(target)