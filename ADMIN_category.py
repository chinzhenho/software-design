# ADMIN_category.py
# Purpose: Defines the abstract Category class and its two concrete implementations.
# Design Pattern: Template Method Pattern (Light usage) - Provides a base class for categories with a common interface.
# Principle: SRP - Only responsible for defining category structure.
# Linked Files: Used by the factories to create category objects.

from abc import ABC, abstractmethod


class Category(ABC):
    def __init__(self, category_name, category_type, description):
        # Common attributes for all categories
        self.category_name = category_name
        self.category_type = category_type
        self.description = description

    @abstractmethod
    def create(self):
        # Abstract method to be defined by subclasses
        pass

class RecyclableCategory(Category):  
    def create(self):
        # Returns a string representation for recyclable category
        return f"Recyclable Category: {self.category_name} ({self.description})"


class NonRecyclableCategory(Category): 
    def create(self):
        # Returns a string representation for non-recyclable category
        return f"Non-Recyclable Category: {self.category_name} ({self.description})"
