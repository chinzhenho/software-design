# ADMIN_category_statistics_view.py
# Purpose: Displays the Recycle Category Statistics in a table.
# Design Pattern: Part of MVC - acts as the View.
# Principle: Single Responsibility Principle (SRP) - Only responsible for displaying statistics data.
# Linked Files:
# - Controlled by AdminCategoryStatsController to render or hide the view.


import tkinter as tk
from tkinter import ttk

class AdminCategoryStatsView:
    def __init__(self, parent):
        # Create the frame and UI elements
        self.frame = tk.Frame(parent)

        self.label = tk.Label(self.frame, text="Recycle Category Statistics", font=("Arial", 16, "bold"))
        self.label.pack(pady=5)

        # Define table columns
        columns = ("no", "category", "user_count")
        self.tree = ttk.Treeview(self.frame, columns=columns, show="headings", height=10)

        # Configure table headers and layout
        self.tree.heading("no", text="No.")
        self.tree.column("no", width=50, anchor="center")

        self.tree.heading("category", text="Category")
        self.tree.column("category", anchor="w", width=200)

        self.tree.heading("user_count", text="Submission Count")
        self.tree.column("user_count", anchor="center", width=120)

        self.tree.pack(padx=10, pady=10, fill="x")

    def render(self, data):
        # Clear existing table rows
        self.tree.delete(*self.tree.get_children())
        # Insert new statistics data
        for idx, row in enumerate(data, start=1):
            self.tree.insert("", "end", values=(idx, *row))
