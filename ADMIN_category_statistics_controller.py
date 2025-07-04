# ADMIN_category_statistics_controller.py
# Purpose: Controller for displaying and hiding the Recycle Category Statistics section.
# Design Pattern: Model-View-Controller (MVC) - acts as the Controller.
# Principle: Single Responsibility Principle (SRP) - Only responsible for controlling the flow between data and view.
# Linked Files:
# - Uses AdminCategoryStatsData (Model) to fetch data.
# - Controls AdminCategoryStatsView (View) to display or hide the statistics section.


from ADMIN_category_statistics_data import AdminCategoryStatsData
from ADMIN_category_statistics_view import AdminCategoryStatsView

class AdminCategoryStatsController:
    def __init__(self, parent):
        self.data_model = AdminCategoryStatsData() # Data handler (Model)
        self.view = AdminCategoryStatsView(parent) # Visual display (View)
        self.displayed = False # Track whether the statistics are currently shown

    def toggle_display(self):
        # Show or hide the statistics section when triggered
        if self.displayed:
            # Hide the view
            self.view.frame.pack_forget()
            self.displayed = False
        else:
            # Fetch statistics data from the database
            stats = self.data_model.get_category_statistics()
            # Pass the data to the view for rendering
            self.view.render(stats) 
            # Show the view
            self.view.frame.pack(pady=10, fill="x")
            self.displayed = True
