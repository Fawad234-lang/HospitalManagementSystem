import tkinter as tk

class BillingWindow:
    def __init__(self, master):
        self.master = master
        master.title("Billing & Payments")

        tk.Label(master, text="Patient Name").pack()
        self.name = tk.Entry(master)
        self.name.pack()

        tk.Label(master, text="Amount").pack()
        self.amount = tk.Entry(master)
        self.amount.pack()

        tk.Button(master, text="Generate Bill", command=self.generate_bill).pack()
        self.result = tk.Label(master)
        self.result.pack()

    def generate_bill(self):
        name = self.name.get()
        amount = self.amount.get()
        self.result.config(text=f"Bill generated for {name} - ${amount}")
