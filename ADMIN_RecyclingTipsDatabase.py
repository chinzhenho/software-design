# ADMIN_RecyclingTipsDatabase.py (Database Layer) (SRP)
# This class handles direct database operations for recycling tips.
# It abstracts all SQL queries related to recycling tips.

from database import Database

class AdminRecyclingTipsDatabase:
    @staticmethod
    def update_recycling_tip(category_id, tip):
        #Updates the recycling tip for a given category.
        db = Database.get_instance()
        query = "UPDATE categories SET tip = %s WHERE category_id = %s"
        db.execute_query(query, (tip, category_id))

    @staticmethod
    def fetch_all_categories():
        # Fetches all categories from the database.
        db = Database.get_instance()
        query = "SELECT category_id, category_name, category_type, description, tip FROM categories"
        return db.fetch_all(query)
