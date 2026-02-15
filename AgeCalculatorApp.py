import tkinter as tk
from tkinter import messagebox
from datetime import date

def calculate_age():
    name = name_var.get().strip()

    if not name:
        messagebox.showerror("Missing Info", "Please enter your name.")
        return

    try:
        day = int(day_var.get())
        month = int(month_var.get())
        year = int(year_var.get())

        birth_date = date(year, month, day)
        today = date.today()

        if birth_date > today:
            messagebox.showerror("Invalid Date", "Birth date cannot be in the future.")
            return

        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        result_label.config(
            text=f"Hi {name}! 🎉\nYou are {age} years old today.",
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid date:\nDay (1-31), Month (1-12), and a real Year."
        )

root = tk.Tk()
root.title("Age Calculator App")
root.geometry("400x400")
root.resizable(False, False)
root.configure(bg="#f4f6fb")

title_label = tk.Label(
    root,
    text="Age Calculator",
    font=("Arial", 18, "bold"),
    bg="#f4f6fb",
    fg="#1f2d3d"
)
title_label.pack(pady=18)

form_frame = tk.Frame(root, bg="#ffffff", bd=2, relief="groove")
form_frame.pack(padx=20, pady=10, fill="x")

name_var = tk.StringVar()
day_var = tk.StringVar()
month_var = tk.StringVar()
year_var = tk.StringVar()

form_frame.columnconfigure(0, weight=1)
form_frame.columnconfigure(1, weight=2)

def make_row(r, text, var, placeholder=""):
    lbl = tk.Label(form_frame, text=text, font=("Arial", 11), bg="#ffffff", fg="#333333", anchor="w")
    ent = tk.Entry(form_frame, textvariable=var, font=("Arial", 11), bd=2, relief="solid")
    lbl.grid(row=r, column=0, sticky="w", padx=12, pady=10)
    ent.grid(row=r, column=1, sticky="ew", padx=12, pady=10)
    if placeholder:
        ent.insert(0, placeholder)

make_row(0, "Name:", name_var, "e.g. John")
make_row(1, "Day:", day_var, "1-31")
make_row(2, "Month:", month_var, "1-12")
make_row(3, "Year:", year_var, "e.g. 2012")

button_frame = tk.Frame(root, bg="#f4f6fb")
button_frame.pack(pady=12)

calc_btn = tk.Button(
    button_frame,
    text="Calculate Age",
    font=("Arial", 11, "bold"),
    bg="#4c7dff",
    fg="white",
    activebackground="#365fda",
    activeforeground="white",
    bd=0,
    padx=18,
    pady=10,
    command=calculate_age
)
calc_btn.pack()

result_label = tk.Label(
    root,
    text="Enter your details above, then click Calculate Age.",
    font=("Arial", 11),
    bg="#f4f6fb",
    fg="#1f2d3d",
    justify="center"
)
result_label.pack(pady=18)

root.mainloop()