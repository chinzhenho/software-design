# ADMIN_commands.py
# Purpose: Defines Command objects for Add, Edit, and Delete operations.
# Design Pattern: Command Pattern - Encapsulates all category operations as objects.
# Principle: SRP - Each class has one responsibility (Add, Edit, or Delete a category).
# Linked Files:
# - Uses CategoryController to perform operations.
# - Used by CommandInvoker to execute and undo commands.

from abc import ABC, abstractmethod
from ADMIN_category_controller import CategoryController

class Command(ABC):
    @abstractmethod
    def execute(self):
        # Abstract method for executing commands
        pass

class AddCategoryCommand(Command):
    def __init__(self, controller: CategoryController, category_name, category_type, description):
        # Stores the necessary data to add a category
        self.controller = controller
        self.category_name = category_name
        self.category_type = category_type
        self.description = description

    def execute(self):
        # Executes the add category operation via controller
        self.controller.add_category(self.category_name, self.category_type, self.description)

class EditCategoryCommand(Command):
    def __init__(self, controller: CategoryController, category_id, category_name, category_type, description):
        # Stores the necessary data to edit a category
        self.controller = controller
        self.category_id = category_id
        self.category_name = category_name
        self.category_type = category_type
        self.description = description

    def execute(self):
        # Executes the edit category operation via controller
        self.controller.update_category(self.category_id, self.category_name, self.category_type, self.description)

class DeleteCategoryCommand(Command):
    def __init__(self, controller, category_id, backup_data):
        # Stores the necessary data to delete a category and restore it (undo)
        self.controller = controller
        self.category_id = category_id
        self.backup = backup_data

    def execute(self):
        # Executes the delete operation via controller
        self.controller.delete_category(self.category_id)

    def undo(self):
        # Restores the deleted category using backup data
        name, type, desc = self.backup
        self.controller.add_category(name, type, desc)
