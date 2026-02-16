from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Cool button!")
root.geometry("300x300")

def handle_click(event):
    messagebox.showerror("Error", "Unable to open file..")

button= Button(text="Click me for a suprise!")
button.pack()

button.bind("<Button-1>", handle_click)

root.mainloop()