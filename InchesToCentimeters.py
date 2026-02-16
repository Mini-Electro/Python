from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Inches to Centimeters Converter")
root.geometry("350x250")

def convert():
    try:
        inches = float(entry.get())
        centimeters = inches * 2.54
        result_label.config(text=f"{centimeters:.2f} cm")
    except ValueError:
        messagebox.showerror("Invaild Input.", "Please Enter a vaild number.")


label = Label(root, text="Enter length in inches:", font=("Arial", 12))
label.pack(pady=5)

entry = Entry(root, width=20)
entry.pack(pady=5)

convert_button = Button(root, text="Convert", command=convert, bg="blue",fg="white")
convert_button.pack(pady=10)

result_label = Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()