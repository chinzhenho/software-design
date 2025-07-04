# ADMIN_category_statistics_data.py
# Purpose: Fetches category submission statistics from the database.
# Design Pattern: Part of MVC - acts as the Model.
# Principle: Single Responsibility Principle (SRP) - Only handles database queries for category statistics.
# Linked Files:
# - Provides data to AdminCategoryStatsController.

from database import Database

class AdminCategoryStatsData:
    def __init__(self):
        self.db = Database.get_instance() # Uses shared database connection (Singleton)

    def get_category_statistics(self):
        # SQL query to count submissions grouped by category
        query = """
            SELECT category, 
                   COUNT(*) AS submission_count
            FROM user_proof 
            GROUP BY category
        """
        return self.db.fetch_all(query) # Returns data to the controller
