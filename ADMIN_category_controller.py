
#ADMIN_category_controller.py
# Purpose: Acts as the controller in the system to handle requests from the UI and interact with the CategoryManager.
# Design Pattern: Factory Method Pattern - Uses CategoryFactory to dynamically create specific category types.
# Principle: SRP - Only responsible for controlling category operations.
# Linked Files:
# - Connects to CategoryManager for database operations.
# - Uses CategoryFactory to create category objects.


from ADMIN_category_factory import CategoryFactory, RecyclableCategoryFactory, NonRecyclableCategoryFactory
from ADMIN_category_manager import CategoryManager
from database import Database

class CategoryController:

    def __init__(self):
        # Initializes CategoryManager with the shared database instance
        db = Database.get_instance()

        self.category_manager = CategoryManager(db)  

    def add_category(self, category_name, category_type, description):
        # Uses the Factory Method Pattern to create the correct category type
        factory = RecyclableCategoryFactory() if category_type == "Recyclable" else NonRecyclableCategoryFactory()
        category = factory.get_category(category_name, category_type, description)
        return self.category_manager.create_category(category)

    def update_category(self, category_id, category_name, category_type, description):
        # Delegates update operation to the CategoryManager
        return self.category_manager.update_category(category_id, category_name, category_type, description)

    def delete_category(self, category_id):
        # Delegates delete operation to the CategoryManager
        return self.category_manager.delete_category(category_id)

    def get_categories(self):
        # Retrieves all categories via the CategoryManager
        return self.category_manager.get_categories()

    def get_category_by_id(self, category_id):
        # Retrieves a specific category by ID directly using the database
        query = "SELECT category_name, category_type, description FROM categories WHERE category_id = %s"
        return self.category_manager.db.fetch_one(query, (category_id,))


