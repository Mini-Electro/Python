import tkinter as tk
from tkinter import messagebox

def calc():
    try:
        p = float(pv.get())
        t = float(tv.get())
        r = float(rv.get())
        if p < 0 or t < 0 or r < 0:
            raise ValueError
        si.set(f"{(p*t*r)/100:.2f}")
    except:
        messagebox.showerror("Error", "Enter valid numbers")

root = tk.Tk()
root.geometry("400x400")
root.title("Interest Calculator App")

pv, tv, rv, si = tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()

for i, (label, var) in enumerate([
    ("Principal", pv),
    ("Time (years)", tv),
    ("Rate (%)", rv),
    ("Simple Interest", si)
]):
    tk.Label(root, text=label).pack()
    tk.Entry(root, textvariable=var).pack()

tk.Button(root, text="Calculate", command=calc).pack(pady=10)
tk.Button(root, text="Exit", command=root.destroy).pack()

root.mainloop()