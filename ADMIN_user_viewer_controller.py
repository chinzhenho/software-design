# ADMIN_user_viewer_controller.py
# Controller class that manages the interaction between the user data (model)
# and the user interface (view). Responsible for toggling the visibility 
# of the user table.
from ADMIN_user_statistics import ADMIN_UserStatistics
from ADMIN_user_table_view import AdminUserTableView # This is the table view file.  # 你需新建这个模块文件

class AdminUserViewerController:
    def __init__(self, parent):
        self.view = AdminUserTableView(parent) # Creates the user table view
        self.stats = ADMIN_UserStatistics() # Creates the user data model
        self.displayed = False # Controls visibility state

    def toggle(self):
        if self.displayed:
            self.view.frame.pack_forget() # Hides the table
            self.displayed = False
        else:
            users = self.stats.get_all_user_details() # Fetches user data
            self.view.render(users) # Passes data to the view
            self.view.frame.pack(pady=10, fill="x") # Shows the table
            self.displayed = True
