# viewTips.py
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from database import Database  # your Database class
from USER_strategy import DisposalContext, GeneralDisposalStrategy
from USER_observer import CategoriesAdmin, UserNotification
from USER_Profile import UserProfilePopup 
from USER_Survey import SurveyPopup  
from USER_FAQ import FAQPopup
from USER_ProofUpload import ProofUploadPopup
from USER_Leaderboard import LeaderboardPopup  
from USER_ShowPrice import MaterialPricePopup
from USER_Location import UserLocationPopup


class UserMainPage(tk.Tk):
    def __init__(self,user_email):
        super().__init__()
        self.title("Recycling System - Main Page")
        self.geometry("400x650")

        self.user_email = user_email  # ✅ Store user email

        # Top frame for Logout button (pack with fill X)
        top_frame = tk.Frame(self)
        top_frame.pack(fill="x", pady=5, padx=5)

        # Logout Button aligned to the far right
        logout_btn = tk.Button(top_frame, text="Logout", fg="white", bg="red", command=self.logout)
        logout_btn.pack(side="right", padx=(0, 5))

        # Button P just to the left of Logout
        button_p = tk.Button(top_frame, text="Profile", bg="light blue", command=self.open_profile_page)
        button_p.pack(side="right")
        

        # Disposal Search (TOP PART)
        self.disposal_context = DisposalContext(GeneralDisposalStrategy())

         # Set up Observer Pattern
        self.admin = CategoriesAdmin()
        self.user = UserNotification(self)
        self.admin.add_user(self.user)
        
        # Search Frame Styling
        search_frame = tk.Frame(self, bg="#e8f0fe", bd=2, relief="groove")
        search_frame.pack(pady=15, padx=10, fill="x")

        tk.Label(search_frame, text="🔍 How to Dispose an Item", font=("Arial", 13, "bold"), bg="#e8f0fe").pack(pady=(10, 5))

        entry_frame = tk.Frame(search_frame, bg="#e8f0fe")
        entry_frame.pack(pady=5)

        self.search_entry = tk.Entry(entry_frame, width=28, font=("Arial", 11), relief="sunken", bd=2)
        self.search_entry.pack(side="left", padx=(10, 5), ipady=4)
        self.search_entry.focus_set()

        self.search_button = tk.Button(entry_frame, text="Search", bg="#4a90e2", fg="white", font=("Arial", 10, "bold"), command=self.search_item)
        self.search_button.pack(side="left", padx=5)

        # Result Label
        self.search_result_label = tk.Label(search_frame, text="", wraplength=340, font=("Arial", 10), bg="#fefefe", fg="#333", justify="left", relief="solid", bd=1)
        self.search_result_label.pack(pady=10, padx=10, fill="x")


        self.after(200, lambda: self.search_entry.focus_set())

        # Check if any new tips and notify
        # Delay notification check slightly after window loads
        self.after(500, self.admin.check_new_tips)


        # View Tips Button
        self.view_tips_button = tk.Button(self, text="View Tips", compound="top", command=self.open_category_type_page, width=20, height=2, bg="#4a90e2", fg="white", font=("Arial", 12, "bold"))
        self.view_tips_button.pack(pady=(20, 10))  # Slightly closer to buttons below

        # Buttons A, B, C, D under View Tips
        self.button_a = tk.Button(self, text="Participate in Survey", width=20, height=2, bg="#4a90e2", fg="white",
                          font=("Arial", 12, "bold"),  command=self.open_survey)
        self.button_a.pack(pady=5)

        self.button_b = tk.Button(self, text="FAQ", width=20, height=2, bg="#4a90e2", fg="white",
                          font=("Arial", 12, "bold"), command=self.open_faq)
        self.button_b.pack(pady=5)

        self.button_c = tk.Button(self, text="Submit Proof", width=20, height=2, bg="#4a90e2", fg="white",
                          font=("Arial", 12, "bold"),  command=self.open_proof_upload)
        self.button_c.pack(pady=5)

        self.button_d = tk.Button(self, text="Leaderboard", width=20, height=2, bg="#4a90e2", fg="white",
                          font=("Arial", 12, "bold"),  command=self.open_leaderboard_popup)
        self.button_d.pack(pady=5)


        # New button to show material prices
        self.material_price_button = tk.Button(self, text="Material Prices", width=20, height=2, bg="#4a90e2", fg="white",
                                               font=("Arial", 12, "bold"), command=self.open_material_price_popup)
        self.material_price_button.pack(pady=5)

        # New button to show user location
        self.user_location_button = tk.Button(self, text="Show My Location", width=20, height=2, bg="#4a90e2", fg="white",
                                              font=("Arial", 12, "bold"), command=self.open_user_location_popup)
        self.user_location_button.pack(pady=5)

    def logout(self):
        self.destroy()
        import LoginSignUp
        LoginSignUp.App().mainloop()

    def open_material_price_popup(self):
        MaterialPricePopup(self)

    def open_user_location_popup(self):
        UserLocationPopup(self)

    def search_item(self):
        item_name = self.search_entry.get()
        if not item_name:
            self.search_result_label.config(text="Please enter an item name.")
            return

        # Get disposal instructions (Strategy Pattern)
        disposal_method = self.disposal_context.get_disposal_instructions(item_name)
        disposal_text = f"🗑️ Item:\n{disposal_method}"

        # Fetch the tip from DB
        db = Database.get_instance()
        query = "SELECT tip FROM categories WHERE category_name = %s"
        result = db.fetch_one(query, (item_name,))

        tip_text = ""
        if result and result[0]:
            tip_text = f"\n\n💡 How to Dispose {item_name}:\n{result[0]}"

        # Combine and display
        full_text = f"{disposal_text}{tip_text}"
        self.search_result_label.config(text=full_text)


    def open_category_type_page(self):
        self.withdraw()
        CategoryTypePage(self)

    def open_profile_page(self):
        UserProfilePopup(self, self.user_email)  # Make sure user_email is stored when user logs in

    def open_survey(self):
        SurveyPopup(self, self.user_email)

    def open_faq(self):
        self.withdraw()  # ✅ Hide the main dashboard
        faq_popup = FAQPopup(self)

        def on_close():
            self.deiconify()  # ✅ Show the dashboard again
            faq_popup.destroy()

        faq_popup.protocol("WM_DELETE_WINDOW", on_close)
    
    def open_proof_upload(self):
        self.withdraw()
        ProofUploadPopup(self, self.user_email)

    def open_leaderboard_popup(self):
        self.withdraw()  # Hide dashboard if needed
        popup = LeaderboardPopup(self)
        popup.protocol("WM_DELETE_WINDOW", lambda: (popup.destroy(), self.deiconify()))




class CategoryTypePage(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Select Category Type")
        self.geometry("400x500")
        self.configure(bg="#f0f4f7")
        self.master = master

        # Top frame for Back button
        top_frame = tk.Frame(self, bg="#f0f4f7")
        top_frame.pack(fill="x", pady=10, padx=10)

        back_btn = tk.Button(top_frame, text="← Back", bg="#ff6666", fg="white", font=("Arial", 10, "bold"), command=self.go_back)
        back_btn.pack(side="left")

        # Title Label
        title_label = tk.Label(self, text="Choose a Category Type", font=("Arial", 14, "bold"), bg="#f0f4f7", fg="#333")
        title_label.pack(pady=(20, 10))

        self.db = Database.get_instance()

        # Category buttons frame
        button_frame = tk.Frame(self, bg="#f0f4f7")
        button_frame.pack(pady=10)

        query = "SELECT DISTINCT category_type FROM categories"
        results = self.db.fetch_all(query)

        if results:
            for row in results:
                category_type = row[0]
                button = tk.Button(
                    button_frame, text=category_type, width=25, height=2,
                    bg="#4a90e2", fg="white", font=("Arial", 11, "bold"),
                    command=lambda ct=category_type: self.open_category_name_page(ct)
                )
                button.pack(pady=8)
        else:
            tk.Label(button_frame, text="No category types found.", bg="#f0f4f7", font=("Arial", 10)).pack()

    def open_category_name_page(self, category_type):
        self.withdraw()
        CategoryNamePage(self, category_type)

    def go_back(self):
        self.destroy()
        self.master.deiconify()



class CategoryNamePage(tk.Toplevel):
    def __init__(self, master, category_type):
        super().__init__(master)
        self.title(f"Categories under {category_type}")
        self.geometry("400x500")
        self.configure(bg="#f8f9fa")
        self.master = master

        top_frame = tk.Frame(self, bg="#f8f9fa")
        top_frame.pack(fill="x", pady=10, padx=10)

        back_btn = tk.Button(top_frame, text="← Back", bg="#ff6666", fg="white", font=("Arial", 10, "bold"), command=self.go_back)
        back_btn.pack(side="left")

        title_label = tk.Label(self, text=f"Categories: {category_type}", font=("Arial", 14, "bold"), bg="#f8f9fa", fg="#333")
        title_label.pack(pady=(20, 10))

        self.db = Database.get_instance()

        button_frame = tk.Frame(self, bg="#f8f9fa")
        button_frame.pack(pady=10)

        query = "SELECT category_name FROM categories WHERE category_type = %s"
        results = self.db.fetch_all(query, (category_type,))

        if results:
            for row in results:
                category_name = row[0]
                button = tk.Button(
                    button_frame, text=category_name, width=25, height=2,
                    bg="#6c5ce7", fg="white", font=("Arial", 11, "bold"),
                    command=lambda cn=category_name: self.open_description_page(cn)
                )
                button.pack(pady=8)
        else:
            tk.Label(button_frame, text="No categories found.", bg="#f8f9fa", font=("Arial", 10)).pack()

    def open_description_page(self, category_name):
        self.withdraw()
        DescriptionPage(self, category_name)

    def go_back(self):
        self.destroy()
        self.master.deiconify()


class DescriptionPage(tk.Toplevel):
    def __init__(self, master, category_name):
        super().__init__(master)
        self.title(f"Description - {category_name}")
        self.geometry("420x450")
        self.configure(bg="#fff")
        self.master = master
        self.category_name = category_name  # Save for tip page

        top_frame = tk.Frame(self, bg="#fff")
        top_frame.pack(fill="x", pady=10, padx=10)

        back_btn = tk.Button(top_frame, text="← Back", bg="#ff6666", fg="white", font=("Arial", 10, "bold"), command=self.go_back)
        back_btn.pack(side="left")

        title_label = tk.Label(self, text=category_name, font=("Arial", 14, "bold"), bg="#fff", fg="#2d3436")
        title_label.pack(pady=(20, 10))

        self.db = Database.get_instance()

        query = "SELECT description FROM categories WHERE category_name = %s"
        result = self.db.fetch_one(query, (category_name,))

        desc_frame = tk.Frame(self, bg="#fff")
        desc_frame.pack(pady=10, padx=20)

        if result:
            description = result[0]
            label = tk.Label(desc_frame, text=description, wraplength=350, justify="left", bg="#dfe6e9", font=("Arial", 11), padx=10, pady=10, relief="groove")
            label.pack(pady=20, fill="both", expand=True)
        else:
            tk.Label(desc_frame, text="No description found.", bg="#fff", font=("Arial", 10)).pack()

        # ✅ Add View Tips Button
        tips_button = tk.Button(self, text="View Tips", bg="#00cec9", fg="white", font=("Arial", 11, "bold"),
                                command=self.open_tip_page)
        tips_button.pack(pady=(10, 20))

    def open_tip_page(self):
        self.withdraw()
        TipsPage(self, self.category_name)

    def go_back(self):
        self.destroy()
        self.master.deiconify()

class TipsPage(tk.Toplevel):
    def __init__(self, master, category_name):
        super().__init__(master)
        self.title(f"Tips - {category_name}")
        self.geometry("420x400")
        self.configure(bg="#fefefe")
        self.master = master

        top_frame = tk.Frame(self, bg="#fefefe")
        top_frame.pack(fill="x", pady=10, padx=10)

        back_btn = tk.Button(top_frame, text="← Back", bg="#ff7675", fg="white", font=("Arial", 10, "bold"),
                             command=self.go_back)
        back_btn.pack(side="left")

        title_label = tk.Label(self, text=f"Tips for {category_name}", font=("Arial", 14, "bold"), bg="#fefefe", fg="#2d3436")
        title_label.pack(pady=(20, 10))

        self.db = Database.get_instance()

        # Fetch tips from DB
        query = "SELECT tip FROM categories WHERE category_name = %s"
        result = self.db.fetch_one(query, (category_name,))

        tip_frame = tk.Frame(self, bg="#fefefe")
        tip_frame.pack(pady=10, padx=20)

        if result and result[0]:
            tip_text = result[0]
            label = tk.Label(tip_frame, text=tip_text, wraplength=350, justify="left", bg="#dff9fb", font=("Arial", 11), padx=10, pady=10, relief="groove")
            label.pack(pady=20, fill="both", expand=True)
        else:
            tk.Label(tip_frame, text="No tips found for this category.", bg="#fefefe", font=("Arial", 10)).pack()

    def go_back(self):
        self.destroy()
        self.master.deiconify()



