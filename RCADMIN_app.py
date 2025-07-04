# app.py
import tkinter as tk
from RCADMIN_material_page import MaterialPage
from RCADMIN_location_page import LocationPage
from RCADMIN_material_reception_page import MaterialReceptionPage
import LoginSignUp 

class RecycleCenterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Recycle Center Management System")
        self.geometry("600x500")

        self.frames = {}

        # --- Top frame for "Pages" label and logout button ---
        top_frame = tk.Frame(self, bg="white")
        top_frame.pack(fill="x")

        # "Pages" label on the left
        pages_label = tk.Label(top_frame, text="Pages", font=("Arial", 12, "bold"), bg="white")
        pages_label.pack(side="left", padx=10, pady=5)

        # Logout button on the right
        logout_btn = tk.Button(top_frame, text="Logout", fg="white", bg="red", command=self.logout)
        logout_btn.pack(side="right", padx=10, pady=5)

        # Add your navigation buttons for pages next to the "Pages" label
        material_btn = tk.Button(top_frame, text="Material Management",bg="light blue", command=lambda: self.show_frame("MaterialPage"))
        material_btn.pack(side="left", padx=5)
        location_btn = tk.Button(top_frame, text="Find Nearby Centers",bg="light blue", command=lambda: self.show_frame("LocationPage"))
        location_btn.pack(side="left", padx=5)
        reception_btn = tk.Button(top_frame, text="Material Reception",bg="light blue", command=lambda: self.show_frame("ReceptionPage"))
        reception_btn.pack(side="left", padx=5)
        
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        # Create frames
        self.frames["MaterialPage"] = MaterialPage(container)
        self.frames["LocationPage"] = LocationPage(container)
        self.frames["ReceptionPage"] = MaterialReceptionPage(container)

        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MaterialPage")  # default first page

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def logout(self):
        self.destroy()
        LoginSignUp.App().mainloop()


