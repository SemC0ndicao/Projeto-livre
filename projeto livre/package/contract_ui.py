import tkinter as tk
from tkinter import ttk, messagebox
from .Contract import Contract
import os
import json

def base_dir():
    return os.path.dirname(os.path.dirname(__file__))

def load_json(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def load_contracts():
    return load_json(os.path.join(base_dir(), "files", "contracts.json"))

def delete_contract(tree):
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Warning", "No contract selected.")
        return

    values = tree.item(selected[0])["values"]
    if not values or len(values) < 2:
        messagebox.showerror("Error", "Invalid contract entry.")
        return

    cpf = str(values[0]).strip()
    tag = str(values[1]).strip()
    if not cpf or not tag:
        messagebox.showerror("Error", "Missing CPF or Animal Tag.")
        return

    success = Contract.delete_contract(cpf, tag)
    if success:
        tree.delete(selected[0])
        messagebox.showinfo("Success", "Contract deleted.")
    else:
        messagebox.showerror("Error", "Contract not found.")

def add_contract(tree):
    adopters = load_json(os.path.join(base_dir(), "files", "adopters.json"))
    animals = load_json(os.path.join(base_dir(), "files", "animals.json"))

    form = tk.Toplevel()
    form.title("Add Contract")
    form.geometry("300x250")

    tk.Label(form, text="Select Adopter (CPF)").pack()
    adopter_cb = ttk.Combobox(form, values=[a["cpf"] for a in adopters])
    adopter_cb.pack()

    tk.Label(form, text="Select Animal (Tag)").pack()
    animal_cb = ttk.Combobox(form, values=[a["tag"] for a in animals])
    animal_cb.pack()

    def save():
        cpf = adopter_cb.get().strip()
        tag = animal_cb.get().strip()
        if not cpf or not tag:
            messagebox.showwarning("Warning", "All fields are required.")
            return
        contract = Contract.new_contract(cpf, tag)
        tree.insert("", tk.END, values=(contract.cpf, contract.animal_tag, contract.date))
        form.destroy()
        messagebox.showinfo("Success", "Contract added.")

    tk.Button(form, text="Save", command=save).pack(pady=20)

def open_contract_window(root):
    win = tk.Toplevel(root)
    win.title("Contracts")
    win.geometry("500x400")

    tree = ttk.Treeview(win, columns=("CPF", "Animal Tag", "Date"), show="headings")
    tree.heading("CPF", text="CPF")
    tree.heading("Animal Tag", text="Animal Tag")
    tree.heading("Date", text="Date")
    tree.pack(fill=tk.BOTH, expand=True)

    for contract in load_contracts():
        tree.insert("", tk.END, values=(contract["cpf"], contract["animal_tag"], contract["date"]))

    btn_frame = tk.Frame(win)
    btn_frame.pack(pady=10)

    ttk.Button(btn_frame, text="Add Contract", command=lambda: add_contract(tree)).pack(side=tk.LEFT, padx=5)
    ttk.Button(btn_frame, text="Delete Selected", command=lambda: delete_contract(tree)).pack(side=tk.LEFT, padx=5)