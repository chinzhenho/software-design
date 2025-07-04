# ADMIN_user_statistics.py
# This class is responsible for fetching user-related data from the database.
# It follows the Single Responsibility Principle (SRP) by focusing only on 
# database interaction, not on any UI or business logic.
from database import Database

class ADMIN_UserStatistics:
    def __init__(self):
        self.db = Database.get_instance() # Gets a singleton database instance

    def get_all_user_details(self):
        # Retrieves all user details, joining user and user_profiles tables to 
        # display complete user information.
        query = """
            SELECT 
                u.username, 
                u.email, 
                IFNULL(up.name, 'N/A') AS name,
                IFNULL(up.phone, 'N/A') AS phone,
                IFNULL(up.gender, 'N/A') AS gender,
                IFNULL(up.age, 'N/A') AS age,
                IFNULL(up.address, 'N/A') AS address
            FROM user u
            LEFT JOIN user_profiles up ON u.email = up.email
        """
        return self.db.fetch_all(query)
