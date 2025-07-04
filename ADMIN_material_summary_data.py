#ADMIN_material_summary_data.py
# Purpose: Fetches total recycled materials data from the database.
# Design Pattern: Part of MVC - acts as the Model.
# Principle: Single Responsibility Principle (SRP) - Only handles database queries for material totals.
# Linked Files:
# - Provides data to AdminMaterialSummaryController.







from database import Database

class AdminMaterialSummaryData:
    def __init__(self):
        self.db = Database.get_instance() # Uses shared database connection (Singleton)

    def get_material_totals(self):
        # SQL query to sum total materials grouped by material name
        query = """
            SELECT material_name, SUM(amount_kg) AS total_kg
            FROM recycle_center_materials
            GROUP BY material_name
        """
        return self.db.fetch_all(query) # Returns data to the controller



