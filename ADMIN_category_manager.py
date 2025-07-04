
# ADMIN_category_manager.py
# Purpose: Handles CRUD operations for categories in the database.
# Design Pattern: None directly, but works as a service layer.
# Principle: SRP - Only manages database operations related to categories.
# Linked Files:
# - Called by CategoryController to execute database tasks.
# - Uses Database Singleton for queries.

class CategoryManager:
    def __init__(self, db):
        # Accepts a shared database instance
        self.db = db 

    def create_category(self, category):
        # Inserts a new category into the database
        query = "INSERT INTO categories (category_name, category_type, description) VALUES (%s, %s, %s)"
        self.db.execute(query, (category.category_name, category.category_type, category.description))
        return True

    def update_category(self, category_id, category_name, category_type, description):
        # Updates an existing category in the database
        query = "UPDATE categories SET category_name = %s, category_type = %s, description = %s WHERE category_id = %s"
        self.db.execute(query, (category_name, category_type, description, category_id))
        return True

    def delete_category(self, category_id):
        # Deletes a category by ID
        query = "DELETE FROM categories WHERE category_id = %s"
        self.db.execute(query, (category_id,))
        return True

    def get_categories(self):
        # Retrieves all categories
        query = "SELECT * FROM categories"
        return self.db.fetch_all(query)

