import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import os
import shutil
from datetime import datetime
from database import Database

class ProofUploadPopup(tk.Toplevel):
    def __init__(self, master, user_email):
        super().__init__(master)
        self.title("Upload Proof to Earn Points")
        self.geometry("450x650")
        self.resizable(False, False)
        self.master = master
        self.user_email = user_email
        self.db = Database.get_instance()

        self.configure(bg="#f0f0f0")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        # Main frame for padding and organization
        self.widgets_frame = tk.Frame(self, bg="#ffffff", padx=20, pady=20, bd=2, relief="groove")
        self.widgets_frame.pack(expand=True, fill="both", padx=20, pady=20)

        tk.Label(self.widgets_frame, text="Upload Proof of Recycling", font=("Arial", 16, "bold"), bg="white").pack(pady=10)

        # Category Selection
        tk.Label(self.widgets_frame, text="Select Category *", font=("Arial", 11), anchor="w", bg="white").pack(fill="x", pady=(15, 5))
        self.category_var = tk.StringVar()
        self.category_dropdown = ttk.Combobox(self.widgets_frame, textvariable=self.category_var, state="readonly", width=40)
        self.category_dropdown.pack(pady=5)
        self.load_categories()

        # Optional Description
        tk.Label(self.widgets_frame, text="Optional Description", font=("Arial", 11), anchor="w", bg="white").pack(fill="x", pady=(15, 5))
        self.description_text = tk.Text(self.widgets_frame, height=4, width=40, font=("Arial", 10), bd=1, relief="solid")
        self.description_text.pack(pady=5)

        # Optional Image Upload
        tk.Label(self.widgets_frame, text="Optional Photo Proof", font=("Arial", 11), anchor="w", bg="white").pack(fill="x", pady=(15, 5))
        self.image_path = None
        self.image_preview_label = tk.Label(self.widgets_frame, bg="white")
        self.image_preview_label.pack(pady=(0, 5))

        img_btn = tk.Button(self.widgets_frame, text="Choose Image", bg="#3498db", fg="white", font=("Arial", 10, "bold"), command=self.select_image, cursor="hand2")
        img_btn.pack(pady=5)
        img_btn.bind("<Enter>", lambda e: img_btn.config(bg="#2980b9"))
        img_btn.bind("<Leave>", lambda e: img_btn.config(bg="#3498db"))

        # Submit Button
        submit_btn = tk.Button(self.widgets_frame, text="Submit Proof", bg="#27ae60", fg="white", font=("Arial", 12, "bold"), command=self.submit_proof, cursor="hand2")
        submit_btn.pack(pady=35, ipadx=10, ipady=5)
        submit_btn.bind("<Enter>", lambda e: submit_btn.config(bg="#1e8449"))
        submit_btn.bind("<Leave>", lambda e: submit_btn.config(bg="#27ae60"))

    def load_categories(self):
        query = "SELECT DISTINCT category_name FROM categories"
        results = self.db.fetch_all(query)
        if results:
            categories = [row[0] for row in results]
            self.category_dropdown['values'] = categories
        else:
            self.category_dropdown['values'] = ["No categories available"]

    def select_image(self):
        filepath = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
        if filepath:
            self.image_path = filepath
            img = Image.open(filepath)
            img.thumbnail((150, 150))
            photo = ImageTk.PhotoImage(img)
            self.image_preview_label.config(image=photo)
            self.image_preview_label.image = photo

    def submit_proof(self):
        category = self.category_var.get()
        description = self.description_text.get("1.0", "end").strip()
        image = self.image_path
        points = 0

        if not category or category == "No categories available":
            messagebox.showwarning("Missing Info", "Please at least select one type of item.")
            return

        # Point calculation
        points = 1
        if description:
            points = 2
        if description and image:
            points = 3

        image_filename = None
        if image:
            # Save image with unique name
            ext = os.path.splitext(image)[1]
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            image_filename = f"{self.user_email.replace('@', '_')}_{timestamp}{ext}"
            save_path = os.path.join("uploaded_images", image_filename)
            os.makedirs("uploaded_images", exist_ok=True)
            shutil.copy(image, save_path)

        # Insert into DB
        insert_query = """
        INSERT INTO user_proof (email, category, description, image_path, points, submitted_at)
        VALUES (%s, %s, %s, %s, %s, NOW())
        """
        self.db.execute(insert_query, (self.user_email, category, description, image_filename, points))
        messagebox.showinfo("Success", f"Proof submitted! You earned {points} point{'s' if points > 1 else ''}.")
        self.destroy()
        self.master.deiconify()

    def on_close(self):
        self.destroy()
        self.master.deiconify()
