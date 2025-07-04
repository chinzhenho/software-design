#ADMIN_material_summary_view.py
# Purpose: Displays the total amount of recycled materials in a table.
# Design Pattern: Part of MVC - acts as the View.
# Principle: Single Responsibility Principle (SRP) - Only responsible for displaying material data.
# Linked Files:
# - Controlled by AdminMaterialSummaryController to render or hide the view.







import tkinter as tk
from tkinter import ttk

class AdminMaterialSummaryView:
    def __init__(self, parent):
        # Create the frame and UI elements
        self.frame = tk.Frame(parent)

        self.label = tk.Label(self.frame, text="Total Amount of Material (kg)", font=("Arial", 16, "bold"))
        self.label.pack(pady=5)

        # Define table columns
        columns = ("no", "material", "total_kg")
        self.tree = ttk.Treeview(self.frame, columns=columns, show="headings", height=10)

        # Configure table headers and layout
        self.tree.heading("no", text="No.")
        self.tree.column("no", width=50, anchor="center")

        self.tree.heading("material", text="Material")
        self.tree.column("material", anchor="w", width=200)

        self.tree.heading("total_kg", text="Total (kg)")
        self.tree.column("total_kg", anchor="center", width=120)

        self.tree.pack(padx=10, pady=10, fill="x")

    def render(self, data):
        # Clear existing table rows
        self.tree.delete(*self.tree.get_children())
        # Insert new material summary data
        for idx, row in enumerate(data, start=1):
            self.tree.insert("", "end", values=(idx, *row))
