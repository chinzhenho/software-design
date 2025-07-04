# ADMIN_Recycling_Tips_Management.py （(UI Layer)(SRP)
# This class manages the User Interface for recycling tips management.
# It focuses only on displaying categories and handling button clicks.
# All business logic is delegated to AdminRecyclingTipsLogic.


import tkinter as tk
from tkinter import messagebox, simpledialog
from ADMIN_RecyclingTipsLogic import AdminRecyclingTipsLogic

class AdminRecyclingTipsManagement:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.logic = AdminRecyclingTipsLogic()
        self.categories_frame = tk.Frame(self.frame)
        self.categories_frame.pack(pady=10)

        self.show_categories()

    def show_categories(self):
        categories = self.logic.db.fetch_all_categories()

        # Clear previous widgets
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Title
        categories_list_label = tk.Label(self.frame, text="Categories List", font=("Arial", 18))
        categories_list_label.pack()

        # Canvas + Scrollbar setup
        canvas_frame = tk.Frame(self.frame)
        canvas_frame.pack()

        canvas = tk.Canvas(canvas_frame, width=1400, height=600)
        scrollbar = tk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="white")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Display categories inside scrollable_frame
        for index, category in enumerate(categories):
            category_id = category[0]
            category_name = category[1]
            category_type = category[2]
            category_description = category[3]
            category_tip = category[4]

            # Category details
            category_label = tk.Label(scrollable_frame, text=f"{category_name} ({category_type}) - {category_description}", anchor="w", font=("Arial", 12), width=80)
            category_label.grid(row=index + 1, column=0, padx=10, pady=10, sticky="w")

            # Display recycling tip
            tip_label = tk.Label(scrollable_frame, text=f"Tip: {category_tip}" if category_tip else "No Tip Available")
            tip_label.grid(row=index + 1, column=1, padx=10, pady=10)

            # Action buttons
            add_button = tk.Button(scrollable_frame, bg="Chartreuse", text="Add Recycling Tip", command=lambda cid=category_id: self.add_recycling_tip(cid))
            add_button.grid(row=index + 1, column=2, padx=10, pady=10)

            edit_button = tk.Button(scrollable_frame, bg="DeepSkyBlue", text="Edit Tip", command=lambda cid=category_id: self.edit_recycling_tip(cid))
            edit_button.grid(row=index + 1, column=3, padx=10, pady=10)

            delete_button = tk.Button(scrollable_frame, bg="red", text="Delete Tip", command=lambda cid=category_id: self.delete_recycling_tip(cid))
            delete_button.grid(row=index + 1, column=4, padx=10, pady=10)


    def add_recycling_tip(self, category_id):
        recycling_tip = simpledialog.askstring("Add Recycling Tip", f"Enter Recycling Tip for category ID: {category_id}")
        if not recycling_tip or recycling_tip.strip() == "":
            messagebox.showwarning("Incomplete Information", "Please enter a valid recycling tip before submitting.")
            return
        self.logic.add_recycling_tip(category_id, recycling_tip.strip())
        messagebox.showinfo("Success", "Recycling Tip Added Successfully!")
        self.show_categories()

    def edit_recycling_tip(self, category_id):
        new_tip = simpledialog.askstring("Edit Recycling Tip", f"Enter new Recycling Tip for category ID: {category_id}")
        if not new_tip or new_tip.strip() == "":
            messagebox.showwarning("Incomplete Information", "Please enter a valid recycling tip before submitting.")
            return
        self.logic.edit_recycling_tip(category_id, new_tip.strip())
        messagebox.showinfo("Success", "Recycling Tip Updated Successfully!")
        self.show_categories()

    def delete_recycling_tip(self, category_id):
        response = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete the recycling tip for this category?")
        if response:
            self.logic.delete_recycling_tip(category_id)
            messagebox.showinfo("Success", "Recycling Tip Deleted Successfully!")
            self.show_categories()



    def refresh(self):
        self.show_categories()
