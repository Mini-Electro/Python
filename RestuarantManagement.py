import tkinter as tk
from tkinter import ttk, messagebox


class RestaurantOrderManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management App")
        self.root.geometry("800x600")

        # Menu with USD prices
        self.menu_items = {
            "FRIES MEAL": 2,
            "LUNCH MEAL": 2,
            "BURGER MEAL": 3,
            "PIZZA MEAL": 4,
            "CHEESE BURGER": 2.5,
            "DRINKS": 1
        }

        self.exchange_rate = 82  # USD to INR

        self.setup_background()

        # Main Frame
        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        ttk.Label(
            frame,
            text="Restaurant Order Management",
            font=("Arial", 20, "bold")
        ).grid(row=0, columnspan=3, padx=10, pady=10)

        self.menu_labels = {}
        self.menu_quantities = {}

        # Menu Items
        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            label = ttk.Label(
                frame,
                text=f"{item} (${price})",
                font=("Arial", 12)
            )
            label.grid(row=i, column=0, padx=10, pady=5)

            self.menu_labels[item] = label

            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)

            self.menu_quantities[item] = quantity_entry

        # Currency Dropdown
        self.currency_var = tk.StringVar()
        self.currency_var.set("USD")

        ttk.Label(
            frame,
            text="Currency",
            font=("Arial", 12)
        ).grid(row=len(self.menu_items) + 1, column=0, padx=10, pady=5)

        currency_dropdown = ttk.Combobox(
            frame,
            textvariable=self.currency_var,
            state="readonly",
            width=18,
            values=("USD", "INR")
        )
        currency_dropdown.grid(row=len(self.menu_items) + 1, column=1, padx=10, pady=5)

        self.currency_var.trace("w", self.update_menu_prices)

        # Order Button
        order_button = ttk.Button(
            frame,
            text="Place Order",
            command=self.place_order
        )
        order_button.grid(row=len(self.menu_items) + 2, columnspan=3, pady=10)

    # ---------------- BACKGROUND ----------------
    def setup_background(self):
        bg_width, bg_height = 800, 600
        canvas = tk.Canvas(self.root, width=bg_width, height=bg_height)
        canvas.pack(fill="both", expand=True)

        try:
            self.bg_image = tk.PhotoImage(
                file="C://Users//User//OneDrive//Desktop//Python//Module1//restuarantimagelol.jpg"
            )
            canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_image)
        except:
            canvas.create_text(
                400, 300,
                text="Background Image Not Found",
                font=("Arial", 20)
            )

    # ---------------- UPDATE PRICES ----------------
    def update_menu_prices(self, *args):
        currency = self.currency_var.get()
        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchange_rate if currency == "INR" else 1

        for item, label in self.menu_labels.items():
            price = self.menu_items[item] * rate
            label.config(text=f"{item} ({symbol}{price})")

    # ---------------- PLACE ORDER ----------------
    def place_order(self):
        total_cost = 0
        order_summary = "Order Summary:\n\n"

        currency = self.currency_var.get()
        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchange_rate if currency == "INR" else 1

        for item, entry in self.menu_quantities.items():
            value = entry.get()

            if value:
                try:
                    quantity = int(value)
                except ValueError:
                    messagebox.showerror("Error", f"Invalid quantity for {item}")
                    return

                if quantity > 0:
                    price = self.menu_items[item] * rate
                    cost = quantity * price
                    total_cost += cost

                    order_summary += (
                        f"{item}: {quantity} x {symbol}{price} = {symbol}{cost}\n"
                    )

        if total_cost > 0:
            order_summary += f"\nTotal Cost: {symbol}{total_cost}"
            messagebox.showinfo("Order Placed", order_summary)
        else:
            messagebox.showerror("Error", "Please order at least one item.")


# ---------------- RUN PROGRAM ----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantOrderManagement(root)
    root.mainloop()

