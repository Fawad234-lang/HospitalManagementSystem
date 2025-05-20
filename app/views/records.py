import tkinter as tk

class RecordsWindow:
    def __init__(self, master):
        self.master = master
        master.title("Medical Records")

        tk.Label(master, text="Patient Name").pack()
        self.name = tk.Entry(master)
        self.name.pack()

        tk.Label(master, text="Diagnosis").pack()
        self.diagnosis = tk.Entry(master)
        self.diagnosis.pack()

        tk.Button(master, text="Save Record", command=self.save_record).pack()
        self.result = tk.Label(master)
        self.result.pack()

    def save_record(self):
        name = self.name.get()
        diagnosis = self.diagnosis.get()
        self.result.config(text=f"Saved record for {name}: {diagnosis}")
