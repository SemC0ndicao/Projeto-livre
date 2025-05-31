import tkinter as tk
from tkinter import ttk, messagebox
from .Adopter import Adopter
import os
import json

def load_adopters():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(base_dir, "files", "adopters.json")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def delete_adopter(tree):
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Warning", "No adopter selected.")
        return

    values = tree.item(selected[0])["values"]
    if not values or len(values) < 1:
        messagebox.showerror("Error", "Invalid adopter entry.")
        return

    cpf = str(values[0]).strip()
    if not cpf:
        messagebox.showerror("Error", "CPF is empty.")
        return

    success = Adopter.delete_adopter(cpf)
    if success:
        tree.delete(selected[0])
        messagebox.showinfo("Success", "Adopter deleted.")
    else:
        messagebox.showerror("Error", "Adopter not found.")

def add_adopter(tree):
    def save():
        cpf = entry_cpf.get().strip()
        name = entry_name.get().strip()
        phone = entry_phone.get().strip()
        if not cpf or not name or not phone:
            messagebox.showwarning("Warning", "All fields are required.")
            return

        adopter = Adopter.new_adopter(cpf, name, phone)
        tree.insert("", tk.END, values=(adopter.cpf, adopter.name, adopter.phone))
        form.destroy()
        messagebox.showinfo("Success", "Adopter added.")

    form = tk.Toplevel()
    form.title("Add Adopter")
    form.geometry("300x200")

    tk.Label(form, text="CPF").pack()
    entry_cpf = tk.Entry(form)
    entry_cpf.pack()

    tk.Label(form, text="Name").pack()
    entry_name = tk.Entry(form)
    entry_name.pack()

    tk.Label(form, text="Phone").pack()
    entry_phone = tk.Entry(form)
    entry_phone.pack()

    tk.Button(form, text="Save", command=save).pack(pady=10)

def open_adopter_window(root):
    win = tk.Toplevel(root)
    win.title("Adopters")
    win.geometry("500x400")

    tree = ttk.Treeview(win, columns=("CPF", "Name", "Phone"), show="headings")
    tree.heading("CPF", text="CPF")
    tree.heading("Name", text="Name")
    tree.heading("Phone", text="Phone")
    tree.pack(fill=tk.BOTH, expand=True)

    for adopter in load_adopters():
        tree.insert("", tk.END, values=(adopter["cpf"], adopter["name"], adopter["phone"]))

    btn_frame = tk.Frame(win)
    btn_frame.pack(pady=10)

    ttk.Button(btn_frame, text="Add Adopter", command=lambda: add_adopter(tree)).pack(side=tk.LEFT, padx=5)
    ttk.Button(btn_frame, text="Delete Selected", command=lambda: delete_adopter(tree)).pack(side=tk.LEFT, padx=5)