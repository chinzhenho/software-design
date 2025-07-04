#ADMIN_survey_results_view.py
# This class handles the display of survey results using a table.


import tkinter as tk
from tkinter import ttk

class AdminSurveyResultsView:
    def __init__(self, parent):
        self.frame = tk.Frame(parent)

        self.label = tk.Label(self.frame, text="Survey Responses", font=("Arial", 16, "bold"))
        self.label.pack(pady=5)

        self.columns = ("no", "email", "q1", "q2", "q3", "q4", "q5", "submitted_at")
        self.tree = ttk.Treeview(self.frame, columns=self.columns, show='headings', height=10)

        self.tree.heading("no", text="No.")
        self.tree.column("no", width=40, anchor="center")

        for col in self.columns[1:]:
            self.tree.heading(col, text=col.upper())
            self.tree.column(col, anchor="w", width=130)

        self.tree.pack(padx=10, pady=10, fill="x")

    def render(self, data):
        self.tree.delete(*self.tree.get_children())
        for idx, row in enumerate(data, start=1):
            self.tree.insert("", "end", values=(idx, *row))
