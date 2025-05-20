import tkinter as tk
from app.services.appointment_service import book_appointment

class AppointmentWindow:
    def __init__(self, master):
        self.master = master
        master.title("Appointment Booking")

        tk.Label(master, text="Patient Name").pack()
        self.patient = tk.Entry(master)
        self.patient.pack()

        tk.Label(master, text="Doctor Name").pack()
        self.doctor = tk.Entry(master)
        self.doctor.pack()

        tk.Label(master, text="Date (YYYY-MM-DD)").pack()
        self.date = tk.Entry(master)
        self.date.pack()

        tk.Button(master, text="Book Appointment", command=self.book).pack()
        self.output = tk.Label(master)
        self.output.pack()

    def book(self):
        result = book_appointment(self.patient.get(), self.doctor.get(), self.date.get())
        self.output.config(text=result)
