import tkinter as tk
from tkinter import messagebox
import bcrypt
from database import Database
from USER_Dashboard import UserMainPage  # Import the main page class

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login System")
        self.geometry("400x450")
        self.configure(bg="#ecf0f1")
        self.resizable(False, False)
        self.current_frame = None
        self.switch_frame(LoginPage)

    def switch_frame(self, frame_class):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = frame_class(self)
        self.current_frame.pack(pady=20)

class LoginPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#ecf0f1")
        tk.Label(self, text="🔐 Login", font=('Helvetica', 20, 'bold'), bg="#ecf0f1", fg="#2c3e50").pack(pady=20)

        self.create_labeled_entry("Email", "email_entry")
        self.create_labeled_entry("Password", "password_entry", show="*")

        self.login_btn = tk.Button(self, text="Login", bg="#3498db", fg="white",
                                   font=("Helvetica", 11, "bold"), command=self.login)
        self.login_btn.pack(pady=15, ipadx=10, ipady=5)
        self.login_btn.bind("<Enter>", lambda e: self.login_btn.config(bg="#2980b9"))
        self.login_btn.bind("<Leave>", lambda e: self.login_btn.config(bg="#3498db"))

        tk.Button(self, text="Sign Up", bg="white", fg="#2c3e50", relief="flat",
                  font=("Helvetica", 10, "underline"),
                  command=lambda: master.switch_frame(SignUpPage)).pack(pady=5)

    def create_labeled_entry(self, label_text, attr_name, show=None):
        tk.Label(self, text=label_text, bg="#ecf0f1", fg="#2c3e50", font=("Helvetica", 11)).pack()
        entry = tk.Entry(self, width=30, font=("Helvetica", 11), show=show)
        entry.pack(pady=5)
        setattr(self, attr_name, entry)

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not email or not password:
            messagebox.showerror("Error", "All fields are required")
            return

        if email == "admin@admin.com" and password == "Admin1234@":
            self.master.destroy()
            import ADMIN_page
            root = tk.Tk()
            app = ADMIN_page.AdminPage(root)
            root.mainloop()
            return

        if email == "rcadmin@rcadmin.com" and password == "Rcadmin1234@":
            self.master.destroy()
            import RCADMIN_app as rc_app
            rc_app.RecycleCenterApp().mainloop()
            return

        db = Database.get_instance()
        user = db.fetch_one("SELECT password FROM user WHERE email = %s", (email,))
        if user and bcrypt.checkpw(password.encode(), user[0].encode()):
            self.master.destroy()
            main_page = UserMainPage(email)
            main_page.mainloop()
        else:
            messagebox.showerror("Login Failed", "Invalid email or password")

class SignUpPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#ecf0f1")
        tk.Label(self, text="📝 Sign Up", font=('Helvetica', 20, 'bold'), bg="#ecf0f1", fg="#2c3e50").pack(pady=20)

        self.entries = {}
        fields = [("Username", "text"), ("Email", "text"), ("Password", "*")]
        for label, show_char in fields:
            self.create_labeled_entry(label, show_char)

        self.register_btn = tk.Button(self, text="Register", bg="#27ae60", fg="white",
                                      font=("Helvetica", 11, "bold"), command=self.register)
        self.register_btn.pack(pady=15, ipadx=10, ipady=5)
        self.register_btn.bind("<Enter>", lambda e: self.register_btn.config(bg="#1e8449"))
        self.register_btn.bind("<Leave>", lambda e: self.register_btn.config(bg="#27ae60"))

        tk.Button(self, text="Back to Login", bg="white", fg="#2c3e50", relief="flat",
                  font=("Helvetica", 10, "underline"),
                  command=lambda: master.switch_frame(LoginPage)).pack(pady=5)

    def create_labeled_entry(self, label_text, show_char):
        tk.Label(self, text=label_text, bg="#ecf0f1", fg="#2c3e50", font=("Helvetica", 11)).pack()
        entry = tk.Entry(self, width=30, font=("Helvetica", 11), show=show_char if show_char != "text" else None)
        entry.pack(pady=5)
        self.entries[label_text] = entry

    def register(self):
        db = Database.get_instance()
        username = self.entries["Username"].get()
        email = self.entries["Email"].get()
        password = self.entries["Password"].get()

        if not username or not email or not password:
            messagebox.showerror("Error", "Please complete all required fields")
            return

        if len(password) < 8 or not any(c.isupper() for c in password) \
                or not any(c.isdigit() for c in password) \
                or not any(c in "!@#$%^&*()-_=+" for c in password):
            messagebox.showerror("Error", "Password must be at least 8 characters,\ninclude uppercase, number, and symbol")
            return

        if db.fetch_one("SELECT email FROM user WHERE email = %s", (email,)):
            messagebox.showerror("Error", "This email is already registered.")
            return

        hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        try:
            db.execute("INSERT INTO user (username, email, password) VALUES (%s, %s, %s)",
                       (username, email, hashed_pw))
            messagebox.showinfo("Success", "Account created! Redirecting to login.")
            self.master.switch_frame(LoginPage)
        except:
            messagebox.showerror("Error", "Registration failed. Please try again later.")

if __name__ == "__main__":
    app = App()
    app.mainloop()
