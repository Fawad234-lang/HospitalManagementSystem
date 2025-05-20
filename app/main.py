import tkinter as tk
from app.views.login import LoginWindow

def main():
    root = tk.Tk()
    root.geometry("400x300")
    root.title("Hospital Management System")
    LoginWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
