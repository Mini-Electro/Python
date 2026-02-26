import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    if (user_choice == "Rock" and computer_choice == "Scissors") or \
       (user_choice == "Paper" and computer_choice == "Rock") or \
       (user_choice == "Scissors" and computer_choice == "Paper"):
        return "User"
    return "Computer"

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    user_choice_label.config(text=f"Your choice: {user_choice}")
    computer_choice_label.config(text=f"Computer choice: {computer_choice}")

    winner = get_winner(user_choice, computer_choice)

    if winner == "User":
        user_score += 1
        result_label.config(text="You win! 🎉")
    elif winner == "Computer":
        computer_score += 1
        result_label.config(text="Computer wins! 🤖")
    else:
        result_label.config(text="It's a tie! 😄")

    score_label.config(text=f"Score: You {user_score}  |  Computer {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0

    user_choice_label.config(text="Your choice: -")
    computer_choice_label.config(text="Computer choice: -")
    result_label.config(text="Click a button to play!")
    score_label.config(text="Score: You 0  |  Computer 0")

root = tk.Tk()
root.geometry("400x400")
root.title("Length Converter App")  # The instructions say to set this title

title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

user_choice_label = tk.Label(root, text="Your choice: -", font=("Arial", 12))
user_choice_label.pack(pady=5)

computer_choice_label = tk.Label(root, text="Computer choice: -", font=("Arial", 12))
computer_choice_label.pack(pady=5)

result_label = tk.Label(root, text="Click a button to play!", font=("Arial", 14, "bold"))
result_label.pack(pady=15)

score_label = tk.Label(root, text="Score: You 0  |  Computer 0", font=("Arial", 12))
score_label.pack(pady=10)

buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=10)

rock_btn = tk.Button(buttons_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=5, pady=5)

paper_btn = tk.Button(buttons_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=5, pady=5)

scissors_btn = tk.Button(buttons_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5, pady=5)

bottom_frame = tk.Frame(root)
bottom_frame.pack(pady=20)

reset_btn = tk.Button(bottom_frame, text="Reset", width=10, command=reset_game)
reset_btn.grid(row=0, column=0, padx=10)

quit_btn = tk.Button(bottom_frame, text="Quit", width=10, command=root.destroy)
quit_btn.grid(row=0, column=1, padx=10)

root.mainloop()