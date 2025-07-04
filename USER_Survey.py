import tkinter as tk
from tkinter import messagebox, ttk
from database import Database

class SurveyPopup(tk.Toplevel):
    def __init__(self, master, user_email):
        super().__init__(master)
        self.master = master
        self.master.withdraw()  # Hide main window
        self.user_email = user_email
        self.db = Database.get_instance()

        self.title("Participate in Survey")
        self.geometry("510x650")
        self.configure(bg='#f5f5f5')

        # --- Title ---
        tk.Label(self, text="📋 Participate in Survey", font=("Helvetica", 20, "bold"),
                 bg='#f5f5f5', fg="#2c3e50").pack(pady=15)

        # Container frame with padding & white background for questions
        container = tk.Frame(self, bg='white', bd=1, relief='solid')
        container.pack(padx=15, pady=10, fill='both', expand=True)

        # Scrollbar support
        canvas = tk.Canvas(container, bg='white', highlightthickness=0)
        scrollbar = ttk.Scrollbar(container, orient='vertical', command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='white')

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

        # Question Variables (empty default)
        self.q1_var = tk.StringVar(value="")
        self.q2_var = tk.StringVar(value="")
        self.q3_var = tk.StringVar(value="")
        self.q4_var = tk.StringVar(value="")

        # Questions with framed sections
        self.create_question(scrollable_frame, "1. How useful do you find the recycling tips?", self.q1_var,
                             ["Very Useful", "Somewhat Useful", "Not Useful"])
        self.create_question(scrollable_frame, "2. How easy is it to find disposal methods?", self.q2_var,
                             ["Very Easy", "Moderate", "Difficult"])
        self.create_question(scrollable_frame, "3. Are the notifications helpful?", self.q3_var,
                             ["Yes, very helpful", "Neutral", "Not helpful"])
        self.create_question(scrollable_frame, "4. Do you want better location-based suggestions?", self.q4_var,
                             ["Yes", "No", "Maybe"])

        # Question 5 (Text suggestion) with label and border
        q5_frame = tk.Frame(scrollable_frame, bg='white', pady=10)
        q5_frame.pack(fill='x', padx=20, pady=(10, 20))
        tk.Label(q5_frame, text="5. Suggestions for improvement:",
                 bg='white', fg="#2c3e50", font=("Helvetica", 12, "bold")).pack(anchor='w', pady=(0, 6))
        self.q5_text = tk.Text(q5_frame, height=4, width=40, font=("Helvetica", 11),
                               bd=1, relief='solid', highlightthickness=1, highlightcolor="#1abc9c")
        self.q5_text.pack(fill='x')

        # Submit Button with rounded-ish style
        self.submit_btn = tk.Button(
            self, text="✅ Submit", bg="#1abc9c", fg="white", font=("Helvetica", 13, "bold"),
            activebackground="#16a085", relief="flat", borderwidth=0, highlightthickness=0,
            command=self.submit_survey
        )
        self.submit_btn.pack(pady=15, ipadx=25, ipady=8)
        self.submit_btn.bind("<Enter>", lambda e: self.submit_btn.config(bg="#16a085"))
        self.submit_btn.bind("<Leave>", lambda e: self.submit_btn.config(bg="#1abc9c"))

        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def create_question(self, parent, question, variable, options):
        # Frame with border around question
        frame = tk.Frame(parent, bg='white', bd=1, relief='solid', padx=15, pady=10)
        frame.pack(fill='x', padx=20, pady=10)

        tk.Label(frame, text=question, bg='white', fg="#2c3e50", font=("Helvetica", 12, "bold")).pack(anchor='w', pady=(0, 6))

        # Radio buttons with hover effect
        for option in options:
            rb = tk.Radiobutton(frame, text=option, variable=variable, value=option,
                                bg='white', fg="#34495e", font=("Helvetica", 11), anchor='w', cursor="hand2",
                                activebackground='white', activeforeground='#1abc9c', selectcolor='#1abc9c')
            rb.pack(anchor='w', pady=3)

    def submit_survey(self):
        q1 = self.q1_var.get()
        q2 = self.q2_var.get()
        q3 = self.q3_var.get()
        q4 = self.q4_var.get()
        q5 = self.q5_text.get("1.0", tk.END).strip()

        if not all([q1, q2, q3, q4]):
            messagebox.showwarning("Incomplete", "Please answer all required questions.")
            return

        try:
            self.db.execute("""
                INSERT INTO survey (email, q1, q2, q3, q4, q5)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (self.user_email, q1, q2, q3, q4, q5))
            messagebox.showinfo("Thank You", "Survey submitted successfully!")
            self.on_close()
        except Exception as e:
            messagebox.showerror("Database Error", f"Could not save survey: {str(e)}")

    def on_close(self):
        self.master.deiconify()
        self.destroy()
