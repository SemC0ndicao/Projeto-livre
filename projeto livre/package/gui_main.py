import tkinter as tk
from tkinter import ttk
from .animal_ui import open_animal_window
from .adopter_ui import open_adopter_window
from .contract_ui import open_contract_window

def menu():
    root = tk.Tk()
    root.title("Animal Adoption Center")
    root.geometry("400x300")
    root.resizable(False, False)

    title = ttk.Label(root, text="Main Menu", font=("Helvetica", 16))
    title.pack(pady=20)

    ttk.Button(root, text="Manage Animals", command=lambda: open_animal_window(root)).pack(pady=5)
    ttk.Button(root, text="Manage Adopters", command=lambda: open_adopter_window(root)).pack(pady=5)
    ttk.Button(root, text="Manage Contracts", command=lambda: open_contract_window(root)).pack(pady=5)
    ttk.Button(root, text="Exit", command=root.destroy).pack(pady=20)

    root.mainloop()

