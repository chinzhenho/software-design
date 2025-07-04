import tkinter as tk

class FAQPopup(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Frequently Asked Questions (FAQ)")
        self.geometry("500x550")
        self.configure(bg="#f0f8ff")

        # Scrollable canvas
        canvas = tk.Canvas(self, bg="#f0f8ff", borderwidth=0, highlightthickness=0)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        self.scrollable_frame = tk.Frame(canvas, bg="#f0f8ff")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # FAQ content
        self.faq_data = {
            "What items can I recycle?": "You can recycle items like paper, plastic bottles, glass, and metals. Please refer to each category for specific instructions.",
            "How do I dispose of hazardous waste?": "Hazardous waste such as batteries, paints, and chemicals should be taken to designated disposal centers.",
            "How do I earn points in the system?": "You earn points by participating in surveys, recycling items properly, and engaging with tips.",
            "Can I update my profile information?": "Yes, go to your profile from the main page to update your details.",
            "Is my data safe in the system?": "Your privacy is protected. All data is stored securely.",
            "Can I participate in multiple surveys?": "Yes, feel free to participate in any number of surveys.",
            "How often is the recycling tips updated?": "Tips are regularly updated by the admin.",
            "Who can I contact for help?": "Use the contact form or email support.",
        }

        self.answer_labels = {}  # Track answer labels to show/hide

        # Create grouped FAQ frames
        for question, answer in self.faq_data.items():
            group = tk.Frame(self.scrollable_frame, bg="#f0f8ff", bd=1, relief="flat")
            group.pack(fill="x", padx=10, pady=5)

            # Question button
            q_btn = tk.Button(group, text=question, font=("Arial", 12, "bold"),
                              fg="#004080", bg="#e6f2ff", anchor="w", relief="raised",
                              command=lambda q=question: self.toggle_answer(q))
            q_btn.pack(fill="x")

            # Hidden answer label
            a_lbl = tk.Label(group, text=answer, font=("Arial", 11),
                             wraplength=450, justify="left", bg="#f0f8ff")
            a_lbl.pack(fill="x", padx=10, pady=(5, 5))
            a_lbl.pack_forget()

            self.answer_labels[question] = a_lbl

    def toggle_answer(self, question):
        label = self.answer_labels[question]
        if label.winfo_ismapped():
            label.pack_forget()
        else:
            label.pack(fill="x", padx=10, pady=(5, 5))
