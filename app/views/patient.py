import tkinter as tk
from app.services.patient_service import add_patient

class PatientWindow:
    def __init__(self, master):
        self.master = master
        master.title("Patient Registration")

        tk.Label(master, text="Name").pack()
        self.name = tk.Entry(master)
        self.name.pack()

        tk.Label(master, text="Age").pack()
        self.age = tk.Entry(master)
        self.age.pack()

        tk.Button(master, text="Register Patient", command=self.register).pack()
        self.output = tk.Label(master)
        self.output.pack()

    def register(self):
        name, age = self.name.get(), self.age.get()
        add_patient(name, age)
        self.output.config(text=f"Registered {name}")
