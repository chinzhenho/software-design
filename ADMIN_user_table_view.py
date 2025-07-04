# ADMIN_user_table_view.py
# This class manages the display (view) of the user table.
# It follows SRP by focusing purely on presenting the data 
# and updating the UI.
import tkinter as tk
from tkinter import ttk

class AdminUserTableView:
    def __init__(self, parent):
        self.frame = tk.Frame(parent) # Creates a frame container for the user table

        # Displays the total number of registered users
        self.total_label = tk.Label(self.frame, text="", font=("Arial", 14, "bold"))
        self.total_label.pack(pady=5)

        # Define table columns
        self.columns = ("no", "username", "email", "name", "phone", "gender", "age", "address")
        self.tree = ttk.Treeview(self.frame, columns=self.columns, show='headings', height=10)

        # Configure each table column with headings and widths
        self.tree.heading("no", text="No.")
        self.tree.column("no", width=5, anchor="center") 

        self.tree.heading("username", text="Username")
        self.tree.column("username", width=150, anchor="w") 

        self.tree.heading("email", text="Email")
        self.tree.column("email", width=100, anchor="w") 

        self.tree.heading("name", text="Name")
        self.tree.column("name", width=130, anchor="w")

        self.tree.heading("phone", text="Phone")
        self.tree.column("phone", width=60, anchor="w")

        self.tree.heading("gender", text="Gender")
        self.tree.column("gender", width=6, anchor="center")  

        self.tree.heading("age", text="Age")
        self.tree.column("age", width=5, anchor="center")  

        self.tree.heading("address", text="Address")
        self.tree.column("address", width=200, anchor="w")  

        # Display the table
        self.tree.pack(padx=10, pady=10, fill="x")

    def render(self, user_data):
        # Renders the user table with the provided user data.
        # Also updates the total user count.
        self.clear_table()
        self.total_label.config(text=f"Total Registered Users: {len(user_data)}")
        for idx, row in enumerate(user_data, start=1):
            self.tree.insert("", "end", values=(idx, *row))

    def clear_table(self):
        # Clears the existing table rows before refreshing new data.
        for row in self.tree.get_children():
            self.tree.delete(row)
