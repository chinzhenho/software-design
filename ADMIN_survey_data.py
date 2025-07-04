#ADMIN_survey_data.py
# This class handles all database interactions related to survey responses.

from database import Database

class AdminSurveyData:
    def __init__(self):
        self.db = Database.get_instance()

    def get_all_survey_responses(self):
        # Fetches all survey responses from the database.
        query = "SELECT email, q1, q2, q3, q4, q5, submitted_at FROM survey"
        return self.db.fetch_all(query)
