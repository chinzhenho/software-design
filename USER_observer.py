from abc import ABC, abstractmethod
from database import Database

# 1. User Interface (formerly Subscriber)
class User(ABC):
    @abstractmethod
    def update(self, admin, data):
        pass

# 2. Admin Interface (formerly Publisher)
class Admin(ABC):
    def __init__(self):
        self._users = []

    def add_user(self, user: User):
        self._users.append(user)

    def remove_user(self, user: User):
        self._users.remove(user)

    def notify_users(self, data):
        for user in self._users:
            user.update(self, data)

# 3. Concrete Admin (CategoriesAdmin)
class CategoriesAdmin(Admin):
    def __init__(self):
        super().__init__()
        self.db = Database.get_instance()
        self.last_tip = None  # Store the last tip checked

    def check_new_tips(self):
        query = "SELECT category_name, category_type, description FROM categories ORDER BY created_at DESC LIMIT 1"
        result = self.db.fetch_one(query)

        if result and result != self.last_tip:
            self.last_tip = result
            self.notify_users(result)

# 4. Concrete User (UserNotification)
class UserNotification(User):
    def __init__(self, app):
        self.app = app  # Tkinter root or frame

    def update(self, admin, data):
        from tkinter import messagebox
        category_name, category_type, description = data
        messagebox.showinfo(
            "New Recycling Tip Available!",
            f"Category Name: {category_name}\nCategory Type: {category_type}\nDescription: {description}"
        )
