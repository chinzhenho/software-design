
#ADMIN_category_factory.py
# Purpose: Implements the Factory Method Pattern to create different types of categories (Recyclable or Non-Recyclable).
# Design Pattern: Factory Method Pattern - Allows creation of specific category types at runtime.
# Principle: SRP - Responsible only for creating category objects.
# Linked Files: Used by CategoryController to create category objects.

from ADMIN_category import Category  

class CategoryFactory:

    def get_category(self, category_name, category_type, description):
        # Abstract method to be overridden by subclasses
        raise NotImplementedError()

class RecyclableCategoryFactory(CategoryFactory):
    def get_category(self, category_name, category_type, description):
        # Creates a RecyclableCategory object
        return RecyclableCategory(category_name, category_type, description)

class NonRecyclableCategoryFactory(CategoryFactory):
    def get_category(self, category_name, category_type, description):
        # Creates a NonRecyclableCategory object
        return NonRecyclableCategory(category_name, category_type, description)



class RecyclableCategory:
    # Represents a recyclable category object
    def __init__(self, category_name, category_type, description):
        self.category_name = category_name
        self.category_type = category_type
        self.description = description


class NonRecyclableCategory:
    # Represents a non-recyclable category object
    def __init__(self, category_name, category_type, description):
        self.category_name = category_name
        self.category_type = category_type
        self.description = description
