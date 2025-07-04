# material_page.py
import tkinter as tk
from tkinter import messagebox
from database import Database
from RCADMIN_material_action import MaterialActionFactory

class MaterialPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.db = Database.get_instance()

        tk.Label(self, text="Material Name:").grid(row=0, column=0, padx=5, pady=5)
        self.material_entry = tk.Entry(self)
        self.material_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self, text="Price:").grid(row=1, column=0, padx=5, pady=5)
        self.price_entry = tk.Entry(self)
        self.price_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self, text="Recycle Center:").grid(row=2, column=0, padx=5, pady=5)
        self.center_entry = tk.Entry(self)
        self.center_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(self, text="Add Material",bg="light green", command=self.add_material).grid(row=3, column=0, pady=10)
        tk.Button(self, text="Update Material",bg="light green", command=self.update_material).grid(row=3, column=1, pady=10)
        tk.Button(self, text="View All Materials",bg="light yellow", command=self.view_materials).grid(row=4, column=0, columnspan=2, pady=5)

        # Persistent Text widget for results
        self.result_text = tk.Text(self, height=15, width=80)
        self.result_text.grid(row=5, column=0, columnspan=2, pady=10)

    def add_material(self):
        name = self.material_entry.get()
        price = self.price_entry.get()
        center = self.center_entry.get()

        if name and price and center:
            action = MaterialActionFactory().get_action("add")
            action.execute(name, price, center)
            messagebox.showinfo("Success", "Material Added.")
        else:
            messagebox.showwarning("Input Error", "Fill all fields.")

    def update_material(self):
        name = self.material_entry.get()
        price = self.price_entry.get()
        center = self.center_entry.get()

        if name and price and center:
            action = MaterialActionFactory().get_action("update")
            action.execute(name, price, center)
            messagebox.showinfo("Success", "Material Updated.")
        else:
            messagebox.showwarning("Input Error", "Fill all fields.")

    def view_materials(self):
        self.result_text.delete("1.0", tk.END)
        db = Database.get_instance()
        results = db.fetch_all("SELECT material_name, price, center_name FROM materials")
        if results:
            self.result_text.insert(tk.END, "Material\tPrice\tRecycle Center\n")
            self.result_text.insert(tk.END, "-"*60 + "\n")
            for row in results:
                self.result_text.insert(tk.END, f"{row[0]}\t{row[1]}\t{row[2]}\n")
        else:
            self.result_text.insert(tk.END, "No materials found.")
        self.result_text.update_idletasks()
