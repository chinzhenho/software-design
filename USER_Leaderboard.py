import tkinter as tk
from tkinter import ttk
from database import Database

class LeaderboardPopup(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Leaderboard")
        self.geometry("450x500")
        self.resizable(False, False)
        self.configure(bg="#f0f0f0")
        self.db = Database.get_instance()

        # Header
        tk.Label(self, text="Top Recyclers", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

        # Leaderboard frame
        self.tree = ttk.Treeview(self, columns=("Email", "Points"), show="headings", height=15)
        self.tree.heading("Email", text="User Email")
        self.tree.heading("Points", text="Points")
        self.tree.column("Email", width=260)
        self.tree.column("Points", width=100, anchor="center")
        self.tree.pack(padx=20, pady=10)

        # Add style for top 3
        self.tree.tag_configure("gold", background="#FFD700")   # Gold
        self.tree.tag_configure("silver", background="#C0C0C0") # Silver
        self.tree.tag_configure("bronze", background="#CD7F32") # Bronze

        self.refresh_data()

    def mask_email(self, email):
        # Show only domain and last part of username
        username, domain = email.split('@')
        if len(username) > 3:
            return f"{'*' * (len(username) - 3)}{username[-3:]}@{domain}"
        else:
            return f"{'*' * len(username)}@{domain}"

    def refresh_data(self):
        # Clear current data
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Query leaderboard data
        query = """
        SELECT email, SUM(points) as total_points
        FROM user_proof
        GROUP BY email
        ORDER BY total_points DESC
        """
        results = self.db.fetch_all(query)

        # Insert new data
        for index, row in enumerate(results):
            email, points = row
            masked_email = self.mask_email(email)
            tag = ""
            if index == 0:
                tag = "gold"
            elif index == 1:
                tag = "silver"
            elif index == 2:
                tag = "bronze"

            self.tree.insert("", "end", values=(masked_email, points), tags=(tag,))
