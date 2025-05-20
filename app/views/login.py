import tkinter as tk
from tkinter import messagebox
from app.services.auth import authenticate_user, register_user
from app.views.dashboard import DashboardWindow

class LoginWindow:
    def __init__(self, master):
        self.master = master
        tk.Label(master, text="Username").pack()
        self.username = tk.Entry(master)
        self.username.pack()

        tk.Label(master, text="Password").pack()
        self.password = tk.Entry(master, show='*')
        self.password.pack()

        tk.Button(master, text="Login", command=self.login).pack()
        tk.Button(master, text="Sign Up", command=self.signup).pack()

    def login(self):
        if authenticate_user(self.username.get(), self.password.get()):
            self.master.destroy()
            root = tk.Tk()
            DashboardWindow(root)
            root.mainloop()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    def signup(self):
        if register_user(self.username.get(), self.password.get()):
            messagebox.showinfo("Success", "User registered")
        else:
            messagebox.showwarning("Error", "User already exists")
