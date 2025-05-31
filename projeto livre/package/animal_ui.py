import tkinter as tk
from tkinter import ttk, messagebox
from .Animal import Animal
import os
import json

def load_animals():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(base_dir, "files", "animals.json")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def delete_animal(tree):
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Warning", "No animal selected.")
        return
    tag = tree.item(selected[0])["values"][0]
    success = Animal.delete_animal(tag)
    if success:
        tree.delete(selected[0])
        messagebox.showinfo("Success", "Animal deleted.")
    else:
        messagebox.showerror("Error", "Animal not found.")

def add_animal(tree):
    def save():
        especie = entry_species.get().strip()
        breed = entry_breed.get().strip()
        gender = entry_gender.get().strip()
        age = entry_age.get().strip()
        if not especie or not breed or not gender or not age.isdigit():
            messagebox.showwarning("Warning", "All fields are required and age must be numeric.")
            return

        animal = Animal.new_animal(especie, int(age), gender, breed)
        tree.insert("", tk.END, values=(animal.tag, animal.especie, animal.breed, animal.admission_date))
        form.destroy()
        messagebox.showinfo("Success", "Animal added.")

    form = tk.Toplevel()
    form.title("Add Animal")
    form.geometry("300x250")

    tk.Label(form, text="Species").pack()
    entry_species = tk.Entry(form)
    entry_species.pack()

    tk.Label(form, text="Breed").pack()
    entry_breed = tk.Entry(form)
    entry_breed.pack()

    tk.Label(form, text="Gender").pack()
    entry_gender = tk.Entry(form)
    entry_gender.pack()

    tk.Label(form, text="Age").pack()
    entry_age = tk.Entry(form)
    entry_age.pack()

    tk.Button(form, text="Save", command=save).pack(pady=10)

def open_animal_window(root):
    win = tk.Toplevel(root)
    win.title("Animals")
    win.geometry("600x400")

    tree = ttk.Treeview(win, columns=("Tag", "Species", "Breed", "Admission"), show="headings")
    tree.heading("Tag", text="Tag")
    tree.heading("Species", text="Species")
    tree.heading("Breed", text="Breed")
    tree.heading("Admission", text="Admission")
    tree.pack(fill=tk.BOTH, expand=True)

    for animal in load_animals():
        tag = animal.get("tag")
        especie = animal.get("especie")
        breed = animal.get("breed")
        admission = animal.get("admission_date", "")
        tree.insert("", tk.END, values=(tag, especie, breed, admission))

    btn_frame = tk.Frame(win)
    btn_frame.pack(pady=10)

    ttk.Button(btn_frame, text="Add Animal", command=lambda: add_animal(tree)).pack(side=tk.LEFT, padx=5)
    ttk.Button(btn_frame, text="Delete Selected", command=lambda: delete_animal(tree)).pack(side=tk.LEFT, padx=5)