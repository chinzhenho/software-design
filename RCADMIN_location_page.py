# location_page.py
import tkinter as tk
from tkinter import messagebox
from RCADMIN_location_services import LocationService

class LocationPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.location_service = LocationService()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Enter Place Name:").pack(pady=5)

        self.place_entry = tk.Entry(self)
        self.place_entry.pack(pady=5)

        tk.Button(self, text="Find Centers",bg="light yellow", command=self.find_centers).pack(pady=5)

        self.text_output = tk.Text(self, height=10, width=50)
        self.text_output.pack(pady=5)

    def find_centers(self):
        place = self.place_entry.get().strip()
        self.text_output.delete("1.0", tk.END)

        if not place:
            messagebox.showerror("Error", "Please enter a place name.")
            return

        centers = self.location_service.get_centers_by_place(place)

        if not centers:
            self.text_output.insert(tk.END, "No recycling centers found in this place.\n")
        else:
            self.text_output.insert(tk.END, f"Centers in {place}:\n\n")
            for center in centers:
                self.text_output.insert(tk.END, f"- {center}\n")