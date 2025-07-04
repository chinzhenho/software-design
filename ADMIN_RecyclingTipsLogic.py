#ADMIN_RecyclingTipsLogic.py (Business Logic Layer)(SRP)
# This class handles all business logic for recycling tips.
# It validates input and calls the database layer to perform updates.

from ADMIN_RecyclingTipsDatabase import AdminRecyclingTipsDatabase

class AdminRecyclingTipsLogic:
    def __init__(self):
        self.db = AdminRecyclingTipsDatabase()

    def add_recycling_tip(self, category_id, tip):
        # Adds a recycling tip after validating input.
        if not tip:
            raise ValueError("Tip cannot be empty.")
        self.db.update_recycling_tip(category_id, tip)

    def edit_recycling_tip(self, category_id, new_tip):
        # Edits a recycling tip after validating input.
        if not new_tip:
            raise ValueError("New Tip cannot be empty.")
        self.db.update_recycling_tip(category_id, new_tip)

    def delete_recycling_tip(self, category_id):
        # Deletes a recycling tip by setting it to NULL.
        self.db.update_recycling_tip(category_id, None)

