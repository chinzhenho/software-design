import tkinter as tk
from tkinter import messagebox
from RCADMIN_material_action import MaterialReceptionHandler

class MaterialReceptionPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.winfo_toplevel().title("Update Received Materials")

        tk.Label(self, text="Recycle Center Name").grid(row=0, column=0)
        self.center_entry = tk.Entry(self)
        self.center_entry.grid(row=0, column=1)

        tk.Label(self, text="Material Name").grid(row=1, column=0)
        self.material_entry = tk.Entry(self)
        self.material_entry.grid(row=1, column=1)

        tk.Label(self, text="Amount (kg)").grid(row=2, column=0)
        self.amount_entry = tk.Entry(self)
        self.amount_entry.grid(row=2, column=1)

        tk.Button(self, text="Submit", command=self.submit_data).grid(row=3, columnspan=2)

        self.handler = MaterialReceptionHandler()

    def submit_data(self):
        center_name = self.center_entry.get()
        material_name = self.material_entry.get()
        try:
            amount_kg = float(self.amount_entry.get())
            self.handler.update_received_material(center_name, material_name, amount_kg)
            messagebox.showinfo("Success", "Material data updated.")
        except ValueError:
            messagebox.showerror("Error", "Amount must be a number.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update material data: {e}")
