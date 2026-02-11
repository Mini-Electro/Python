from tkinter import *
from datetime import date


# Create window
root = Tk()
root.title("Getting started with Widgets")
root.geometry("400x300")

# Add widgets
# add label
lbl = Label(text="Hey There!", fg="white", bg="#072F5F", height=1, width=300)


# Add label for getting name as input from user
# Use entry widget to create text box for user to enter details
name_lbl = Label(text="Full Name", bg="#3895D3")
name_entry = Entry()

# Function to display a message
def display():
    
    name = name_entry.get()


    global message
    message = "Welcome to the Application! \nToday's date is: "
    greet = "Hello " +name+"\n"


    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

# Add a Text widget to display information
text_box = Text(height=3)

# Add a button and give value of command as name of the function
btn = Button(text="Begin", command=display, height=1, bg="#1261a0", fg="white")


lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

# Start the GUI event loop
root.mainloop()