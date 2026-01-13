import random

def guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
                continue

            difference = abs(secret_number - guess)

            if difference == 0:
                print(f"Correct! You guessed the number in {attempts} attempts.")
                break
            elif difference <= 3:
                print(" Almost there! Very close!")
            elif difference <= 7:
                print(" Close! Keep going.")
            elif guess < secret_number:
                print("⬆ Too low. Try higher.")
            else:
                print("⬇ Too high. Try lower.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")

guessing_game()
