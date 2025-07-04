import tkinter as tk
from tkinter import messagebox
from USER_ProfileManager import UserProfileManager  # SRP: Logic separated

class UserProfilePopup(tk.Toplevel):
    def __init__(self, master, user_email):
        super().__init__(master)
        self.master.withdraw()  # Hide main window
        self.title("User Profile")
        self.geometry("420x520")
        self.configure(bg="#ecf0f1")  # Light grey background

        self.master = master
        self.user_email = user_email
        self.profile_manager = UserProfileManager()

        # Title Label
        tk.Label(self, text="👤 User Profile", font=("Helvetica", 18, "bold"), bg="#ecf0f1", fg="#2c3e50").pack(pady=15)

        # Email (read-only)
        tk.Label(self, text="Email:", bg="#ecf0f1", fg="#2c3e50", font=("Helvetica", 11)).pack()
        self.email_entry = tk.Entry(self, width=40, font=("Helvetica", 11))
        self.email_entry.pack(pady=5)
        self.email_entry.insert(0, self.user_email)
        self.email_entry.configure(state='disabled')

        # Variables
        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.gender_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.address_var = tk.StringVar()

        # Frame for fields
        frame = tk.Frame(self, bg="#ecf0f1")
        frame.pack(pady=10)

        # Create fields
        self.create_label_entry(frame, "Full Name", self.name_var)
        self.create_label_entry(frame, "Phone Number", self.phone_var)
        self.create_label_entry(frame, "Gender", self.gender_var)
        self.create_label_entry(frame, "Age", self.age_var)
        self.create_label_entry(frame, "Address", self.address_var)

        # Save Button
        self.save_btn = tk.Button(
            frame,
            text="💾 Save Profile",
            bg="#1abc9c",
            fg="white",
            font=("Helvetica", 11, "bold"),
            activebackground="#16a085",
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            command=self.save_profile
        )
        self.save_btn.pack(pady=20, ipadx=20, ipady=6)

        # Hover effect
        self.save_btn.bind("<Enter>", lambda e: self.save_btn.config(bg="#16a085"))
        self.save_btn.bind("<Leave>", lambda e: self.save_btn.config(bg="#1abc9c"))

        self.load_existing_profile()
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.master.deiconify()  # Show main window again
        self.destroy()

    def create_label_entry(self, parent, label_text, text_var):
        tk.Label(parent, text=label_text + ":", bg="#ecf0f1", fg="#2c3e50", font=("Helvetica", 11)).pack()
        entry = tk.Entry(parent, textvariable=text_var, width=40, font=("Helvetica", 11))
        entry.pack(pady=5)

    def load_existing_profile(self):
        result = self.profile_manager.load_profile(self.user_email)
        if result:
            self.name_var.set(result[0] or "")
            self.phone_var.set(result[1] or "")
            self.gender_var.set(result[2] or "")
            self.age_var.set(result[3] or "")
            self.address_var.set(result[4] or "")

    def save_profile(self):
        name = self.name_var.get().strip()
        phone = self.phone_var.get().strip()
        gender = self.gender_var.get().strip()
        age = self.age_var.get().strip()
        address = self.address_var.get().strip()

        if not all([name, phone, gender, age, address]):
            messagebox.showwarning("Validation Error", "Please fill in all the fields.")
            return

        data = {
            "email": self.user_email,
            "name": name,
            "phone": phone,
            "gender": gender,
            "age": age,
            "address": address
        }

        self.profile_manager.save_profile(data)
        messagebox.showinfo("Success", "Profile saved successfully.")
        self.master.deiconify()  # Show main window again
        self.destroy()
