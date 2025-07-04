import tkinter as tk
from tkinter import messagebox
import requests
from RCADMIN_location_services import LocationService

class UserLocationPopup(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Your Location")
        self.geometry("480x350")
        self.configure(bg="#f0f4f7")

        self.location_service = LocationService()

        self.location_label = tk.Label(self, text="Detecting your location...", bg="#f0f4f7", font=("Arial", 12))
        self.location_label.pack(pady=10)

        self.centers_text = tk.Text(self, height=10, width=50)
        self.centers_text.pack(pady=10)

        self.manual_label = tk.Label(self, text="Or enter your location manually:", bg="#f0f4f7", font=("Arial", 11))
        self.manual_label.pack(pady=(10, 0))

        self.manual_entry = tk.Entry(self, width=30)
        self.manual_entry.pack(pady=5)

        self.search_button = tk.Button(self, text="Find Centers",bg="light yellow", command=self.find_centers_manual)
        self.search_button.pack(pady=5)

        self.detect_location()

    def detect_location(self):
        try:
            response = requests.get("http://ip-api.com/json/")
            data = response.json()
            if data['status'] == 'success':
                # Use region or city mapping to general places like Puchong, Cyberjaya
                city = data.get('city', '').lower()
                region = data.get('regionName', '').lower()
                country = data.get('country', '')
                # Map detected city/region to general places in database
                general_place = self.map_to_general_place(city, region)
                location_str = general_place if general_place else f"{city}, {region}, {country}"
                self.location_label.config(text=f"Detected Location: {location_str}")
                self.find_centers(location_str)
            else:
                self.location_label.config(text="Could not detect location.")
        except Exception as e:
            self.location_label.config(text="Error detecting location.")
            print(f"Location detection error: {e}")

    def map_to_general_place(self, city, region):
        # Mapping of specific cities/regions to general places in the database
        place_map = {
            "puchong": "Puchong",
            "cyberjaya": "Cyberjaya",
            "putrajaya": "Putrajaya",
            "kuala lumpur": "Kuala Lumpur",
            "selangor": "Selangor",
            "petaling": "Petaling",
            "damansara": "Damansara",
        }
        # Check city first
        for key in place_map:
            if key in city:
                return place_map[key]
        # Check region if city not matched
        for key in place_map:
            if key in region:
                return place_map[key]
        return None

    def find_centers(self, location):
        self.centers_text.delete("1.0", tk.END)
        centers = self.location_service.get_centers_by_place(location)
        if centers:
            self.centers_text.insert(tk.END, f"Recycling Centers near {location}:\n\n")
            for center in centers:
                self.centers_text.insert(tk.END, f"- {center}\n")
        else:
            self.centers_text.insert(tk.END, f"No recycling centers found near {location}.")

    def find_centers_manual(self):
        location = self.manual_entry.get().strip()
        if not location:
            messagebox.showerror("Error", "Please enter a location.")
            return
        self.location_label.config(text=f"Manual Location: {location}")
        self.find_centers(location)
