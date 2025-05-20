import tkinter as tk
from app.views.patient import PatientWindow
from app.views.doctor import DoctorWindow
from app.views.appointment import AppointmentWindow
from app.views.records import RecordsWindow
from app.views.billing import BillingWindow

class DashboardWindow:
    def __init__(self, master):
        self.master = master
        master.title("Admin Dashboard")

        buttons = [
            ("Patient Management", PatientWindow),
            ("Doctor Management", DoctorWindow),
            ("Appointment Booking", AppointmentWindow),
            ("Medical Records", RecordsWindow),
            ("Billing", BillingWindow),
        ]

        for (text, command) in buttons:
            tk.Button(master, text=text, command=lambda cmd=command: self.open_window(cmd)).pack(pady=5)

    def open_window(self, window_class):
        self.master.destroy()
        root = tk.Tk()
        window_class(root)
        root.mainloop()
