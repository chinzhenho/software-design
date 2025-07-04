import tkinter as tk
from tkinter import messagebox
from database import Database

class MaterialPricePopup(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Material Prices")
        self.geometry("500x400")
        self.configure(bg="#f0f4f7")

        self.db = Database.get_instance()

        self.result_text = tk.Text(self, height=20, width=60)
        self.result_text.pack(padx=10, pady=10)

        self.load_material_prices()

    def load_material_prices(self):
        self.result_text.delete("1.0", tk.END)
        query = "SELECT material_name, price, center_name FROM materials"
        results = self.db.fetch_all(query)
        if results:
            self.result_text.insert(tk.END, "Material\tPrice\tRecycle Center\n")
            self.result_text.insert(tk.END, "-"*50 + "\n")
            for row in results:
                self.result_text.insert(tk.END, f"{row[0]}\t{row[1]}\t{row[2]}\n")
            self.result_text.update_idletasks()
        else:
            self.result_text.insert(tk.END, "No materials found.")
