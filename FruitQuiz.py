import random

class FruitQuiz:
    
    def __init__(self):


        # Create a dictionary of fruits as keys and color as value
        self.Fruits = {'apple':'red',
                       'orange':'orange',
                       'watermelon':'green',
                       'banana':'yellow',}
        
    def quiz(self):
        while (True):

            fruit, color = random.choice(list(self.Fruits.items()))
            print("What is the color of {}".format(fruit))
            user_answer = input()

            if (user_answer.lower() == color):
                print("Correct answer!")
            else:
                print("Incorrect answer.")

            option = int(input("enter 0 if you want to play again, otherwise enter 1: "))
            if (option):
                break

print("Welcome to fruit quiz!")
fq = FruitQuiz()
fq.quiz()