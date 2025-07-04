# strategy.py

from abc import ABC, abstractmethod
from database import Database  # Using your Database class

# 1. Strategy Interface
class DisposalStrategy(ABC):
    @abstractmethod
    def get_disposal_method(self, item_name):
        pass

# 2. Concrete Strategy for General Items
class GeneralDisposalStrategy(DisposalStrategy):
    def get_disposal_method(self, item_name):
        db = Database.get_instance()
        query = "SELECT description FROM categories WHERE category_name = %s"
        result = db.fetch_one(query, (item_name,))
        if result:
            return result[0]
        else:
            return "No disposal method found for this item."

# 3. Context
class DisposalContext:
    def __init__(self, strategy: DisposalStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: DisposalStrategy):
        self._strategy = strategy

    def get_disposal_instructions(self, item_name):
        return self._strategy.get_disposal_method(item_name)
