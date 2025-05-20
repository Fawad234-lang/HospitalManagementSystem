import tkinter as tk
from app.services.doctor_service import add_doctor

class DoctorWindow:
    def __init__(self, master):
        self.master = master
        master.title("Doctor Management")

        tk.Label(master, text="Name").pack()
        self.name = tk.Entry(master)
        self.name.pack()

        tk.Label(master, text="Specialty").pack()
        self.specialty = tk.Entry(master)
        self.specialty.pack()

        tk.Button(master, text="Add Doctor", command=self.add).pack()
        self.output = tk.Label(master)
        self.output.pack()

    def add(self):
        name, specialty = self.name.get(), self.specialty.get()
        add_doctor(name, specialty)
        self.output.config(text=f"Added Dr. {name} ({specialty})")
