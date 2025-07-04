# location_services.py
from database import Database

class LocationService:
    def __init__(self):
        self.db = Database.get_instance()

    def get_centers_by_place(self, place):
        query = "SELECT center_name FROM recycling_centers WHERE location_name = %s"
        results = self.db.fetch_all(query, (place,))
        return [center[0] for center in results]