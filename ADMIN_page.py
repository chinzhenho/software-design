# ADMIN_page.py

# Import necessary modules from tkinter for GUI components
import tkinter as tk
from tkinter import messagebox

# Import controller and command classes used in the admin page
from ADMIN_category_controller import CategoryController  
from ADMIN_command_invoker import CommandInvoker  
from ADMIN_commands import AddCategoryCommand, EditCategoryCommand, DeleteCategoryCommand  

# Import database connection
from database import Database

# Import other admin management
from ADMIN_Recycling_Tips_Management import AdminRecyclingTipsManagement
from ADMIN_user_statistics import ADMIN_UserStatistics
from ADMIN_user_viewer_controller import AdminUserViewerController
from ADMIN_survey_results_controller import AdminSurveyResultsController
from ADMIN_category_statistics_controller import AdminCategoryStatsController
from ADMIN_material_summary_controller import AdminMaterialSummaryController

# Import login/signup page
import LoginSignUp  


class AdminPage:
    def __init__(self, root):
        # Initialize the main admin page
        self.root = root
        self.root.title("Admin Dashboard")
        self.root.state("zoomed") # Full screen window

        # Initialize additional controllers for viewing and statistics
        self.user_viewer = AdminUserViewerController(self.root)
        self.survey_results_controller = AdminSurveyResultsController(self.root)
        self.category_stats_controller = AdminCategoryStatsController(self.root)
        self.material_summary_controller = AdminMaterialSummaryController(self.root)

        # Create a frame for the logout button and pack it to the top, fill X
        top_frame = tk.Frame(self.root)
        top_frame.pack(side="top", fill="x")

        # Logout Button aligned to the far right in the top_frame
        logout_btn = tk.Button(top_frame, text="Logout", fg="white", bg="red", command=self.logout)
        logout_btn.pack(side="right", padx=(0, 10), pady=10)

        # Initialize category controller and command invoker
        self.controller = CategoryController()
        self.invoker = CommandInvoker()  
        
        # Track whether the category management section is visible
        self.is_category_visible = False  

        # Track the currently selected category ID for editing
        self.selected_category_id = None

        # Call function to create all the UI widgets
        self.create_widgets()

    def create_widgets(self):
        # Create title label for the admin page
        self.title_label = tk.Label(self.root, text="Admin Dashboard", font=("Arial", 24))
        self.title_label.pack(pady=10)

        # Create frame to hold main navigation buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        # Button to show/hide category management section
        self.manage_categories_button = tk.Button(self.button_frame, bg="sky blue", text="Manage Categories", command=self.show_category_management, font=("Arial", 12))
        self.manage_categories_button.grid(row=0, column=0, padx=5)


        # Button to open recycling tips management page
        self.admin_recycling_tips_management_button = tk.Button(self.button_frame, bg="sky blue", text="Manage Recycling Tips", command=self.show_recycling_tips_management, font=("Arial", 12))
        self.admin_recycling_tips_management_button.grid(row=0, column=1, padx=5)

        # Button to show total user details
        self.view_total_users_button = tk.Button(self.button_frame, bg="sky blue", text="View Total Users",command=self.user_viewer.toggle,font=("Arial", 12))
        self.view_total_users_button.grid(row=0, column=2, padx=5)

        # Button to display survey results
        self.view_survey_results_button = tk.Button(self.button_frame, bg="sky blue", text="View Survey Results",command=self.survey_results_controller.toggle_display,font=("Arial", 12))
        self.view_survey_results_button.grid(row=0, column=6, padx=5)

        # Button to display recycle category statistics
        self.view_category_stats_button = tk.Button(self.button_frame, bg="sky blue", text="View Recycle Statistics",command=self.category_stats_controller.toggle_display,font=("Arial", 12))
        self.view_category_stats_button.grid(row=0, column=7, padx=5)

        # Button to display material received from rcadmin
        self.view_material_summary_button = tk.Button(self.button_frame, bg="sky blue", text="View Material Summary",command=self.material_summary_controller.toggle_display,font=("Arial", 12))
        self.view_material_summary_button.grid(row=0, column=8, padx=5)




        # Create form frame to add new categories
        self.add_category_frame = tk.Frame(self.root)

        # Label and input for category name
        self.category_name_label = tk.Label(self.add_category_frame, text="Category Name:")
        self.category_name_label.grid(row=0, column=0, padx=10, pady=10)
        self.category_name_entry = tk.Entry(self.add_category_frame)
        self.category_name_entry.grid(row=0, column=1, padx=10, pady=10)

        # Radio buttons to select category type
        self.category_type_label = tk.Label(self.add_category_frame, text="Is Recyclable:")
        self.category_type_label.grid(row=1, column=0, padx=10, pady=10)
        self.category_type_var = tk.StringVar(value="Recyclable")
        self.category_type_recyclable = tk.Radiobutton(self.add_category_frame, text="Yes", variable=self.category_type_var, value="Recyclable")
        self.category_type_recyclable.grid(row=1, column=1, padx=10, pady=10)
        self.category_type_non_recyclable = tk.Radiobutton(self.add_category_frame, text="No", variable=self.category_type_var, value="Non-Recyclable")
        self.category_type_non_recyclable.grid(row=1, column=2, padx=10, pady=10)

        # Label and input for category description
        self.description_label = tk.Label(self.add_category_frame, text="Description:")
        self.description_label.grid(row=2, column=0, padx=10, pady=10)
        self.description_entry = tk.Entry(self.add_category_frame)
        self.description_entry.grid(row=2, column=1, padx=10, pady=10)

        # Button to add the category to the database
        self.add_category_button = tk.Button(self.add_category_frame, bg = "Chartreuse", text="Add Category", command=self.add_category)
        self.add_category_button.grid(row=3, column=1, pady=10)

        
        # Create frame to display categories list with a scrollbar
        self.categories_frame = tk.Frame(self.root)
        
        # Frame to hold the categories list label and undo button
        self.categories_header_frame = tk.Frame(self.categories_frame)
        self.categories_header_frame.pack(pady=10)

        # Label for categories list
        self.categories_list_label = tk.Label(self.categories_header_frame, text="Categories List", font=("Arial", 18))
        self.categories_list_label.pack(side="left")

        # Undo button to reverse last delete
        self.undo_button = tk.Button(self.categories_header_frame, bg="pink", text="Undo Delete", command=self.undo_last_command)
        self.undo_button.pack(side="left", padx=10)

        # Create canvas and scrollbar for scrollable category list
        self.canvas = tk.Canvas(self.categories_frame, height=600, width=1000)
        self.scrollbar = tk.Scrollbar(self.categories_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="white")

        # Update scroll region when the frame size changes
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        # Embed the scrollable frame in the canvas
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw", width=1000)

        # Connect scrollbar to canvas
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Initially load the categories list
        self.show_categories()

    def show_category_management(self):
        # Toggle visibility of category management section
        if self.is_category_visible:
            self.add_category_frame.pack_forget()
            self.categories_frame.pack_forget()
            self.is_category_visible = False
        else:
            self.add_category_frame.pack(pady=20)
            self.categories_frame.pack(pady=20)
            self.is_category_visible = True

    def show_recycling_tips_management(self):
        # Show or hide the recycling tips management frame
        if not hasattr(self, 'recycling_tips_management') or self.recycling_tips_management is None:
            self.recycling_tips_management = AdminRecyclingTipsManagement(self.root)
        else:
            if self.recycling_tips_management.frame.winfo_ismapped():
                self.recycling_tips_management.frame.pack_forget()
            else:
                # Refresh the category list in recycling tips management
                self.recycling_tips_management.refresh()
                self.recycling_tips_management.frame.pack(pady=20)


    


    def add_category(self):
        # Get input values from the form
        category_name = self.category_name_entry.get()
        category_type = self.category_type_var.get()
        description = self.description_entry.get()

        # Validate category name length
        if not category_name or len(category_name) < 3:
            messagebox.showwarning("Input Error", "Category name must be at least 3 characters long!")
            return

        # Create and execute the add category command
        add_command = AddCategoryCommand(self.controller, category_name, category_type, description)
        self.invoker.execute_command(add_command)

        messagebox.showinfo("Success", "Category Added Successfully!")

        # Clear input fields and refresh category list
        self.clear_fields()
        self.show_categories()

    def show_categories(self):
        # Fetch all categories from the database
        db = Database.get_instance()

        query = "SELECT * FROM categories"
        categories = db.fetch_all(query)

        # Clear existing widgets in the scrollable frame
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        # Display each category with edit and delete buttons
        for index, category in enumerate(categories):
            category_id = category[0]
            category_name = category[1]
            category_type = category[2]
            category_description = category[3]

            category_label = tk.Label(self.scrollable_frame, text=f"{category_name} ({category_type}) - {category_description}", anchor="w", font=("Arial", 12), width=95)

            category_label.grid(row=index, column=0, padx=10, pady=10, sticky="w")

            edit_button = tk.Button(self.scrollable_frame, bg="DeepSkyBlue", text="Edit", command=lambda cid=category_id: self.edit_category(cid))
            edit_button.grid(row=index, column=1, padx=10, pady=10)

            delete_button = tk.Button(self.scrollable_frame, bg="red", text="Delete", command=lambda cid=category_id: self.delete_category(cid))
            delete_button.grid(row=index, column=2, padx=10, pady=10)


            
    def clear_fields(self):
        # Clear input fields in the form
        self.category_name_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)

    def delete_category(self, category_id):
        # Retrieve category data before deleting for backup
        backup_data = self.controller.get_category_by_id(category_id)

        if not backup_data:
            messagebox.showerror("Error", "Category not found!")
            return

        # Create and execute delete command
        delete_command = DeleteCategoryCommand(self.controller, category_id, backup_data)
        self.invoker.execute_command(delete_command)

        messagebox.showinfo("Success", "Category Deleted Successfully!")
        self.show_categories()


    def edit_category(self, category_id):
        # Confirm if the user really wants to edit
        response = messagebox.askyesno("Confirm Edit", "Are you sure you want to edit this category?")
        if response:
            db = Database.get_instance()
            query = "SELECT * FROM categories WHERE category_id = %s"
            category = db.fetch_one(query, (category_id,))
            self.selected_category_id = category_id

            # Pre-fill form with selected category data
            self.category_name_entry.delete(0, tk.END)
            self.category_name_entry.insert(0, category[1])
            self.category_type_var.set(category[2])
            self.description_entry.delete(0, tk.END)
            self.description_entry.insert(0, category[3])

            # Change add button to update mode
            self.add_category_button.config(text="Update Category", command=self.update_category)

    def update_category(self):
        # Get updated form data
        category_name = self.category_name_entry.get()
        category_type = self.category_type_var.get()
        description = self.description_entry.get()

        if not category_name or len(category_name) < 3:
            messagebox.showwarning("Input Error", "Category name must be at least 3 characters long!")
            return

        # Create and execute edit command
        edit_command = EditCategoryCommand(self.controller, self.selected_category_id, category_name, category_type, description)
        self.invoker.execute_command(edit_command)

        messagebox.showinfo("Success", "Category Updated Successfully!")
        self.clear_fields()
        self.show_categories()

        # Change button back to add mode
        self.add_category_button.config(text="Add Category", command=self.add_category)

    def undo_last_command(self):
        # Undo the last executed command
        self.invoker.undo_last()
        self.show_categories()

    def logout(self):
        # Destroy current window and return to login page
        self.root.destroy()
        LoginSignUp.App().mainloop()


