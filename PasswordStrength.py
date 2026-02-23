import tkinter as tk

def check_strength():
    pwd = password_entry.get()
    length = len(pwd)

    if length > 12:
        strength_text = "Very Strong"
        strength_color = "dark green"
    elif length > 8:
        strength_text = "Strong"
        strength_color = "light green"
    elif length >= 6:
        strength_text = "Medium"
        strength_color = "yellow"
    else:
        strength_text = "Weak"
        strength_color = "red"

    result_label.config(text=f"Strength: {strength_text}", fg=strength_color)

def clear_fields():
    password_entry.delete(0, tk.END)
    result_label.config(text="Strength: ", fg="black")

root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x400")

title_label = tk.Label(root, text="Password Strength Checker", font=("Arial", 16, "bold"))
title_label.pack(pady=20)

info_label = tk.Label(root, text="Enter a password (strength is based on length only):", font=("Arial", 10))
info_label.pack(pady=10)

password_entry = tk.Entry(root, width=30, font=("Arial", 12), show="*")
password_entry.pack(pady=10)

check_button = tk.Button(root, text="Check Strength", font=("Arial", 12), command=check_strength)
check_button.pack(pady=10)

result_label = tk.Label(root, text="Strength: ", font=("Arial", 14, "bold"))
result_label.pack(pady=20)

clear_button = tk.Button(root, text="Clear", font=("Arial", 12), command=clear_fields)
clear_button.pack(pady=10)

root.bind("<Return>", lambda event: check_strength())

root.mainloop()