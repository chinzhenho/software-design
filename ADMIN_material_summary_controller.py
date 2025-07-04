#ADMIN_material_summary_controller.py
# Purpose: Controller for displaying and hiding the Total Material Summary section.
# Design Pattern: Model-View-Controller (MVC) - acts as the Controller.
# Principle: Single Responsibility Principle (SRP) - Only controls the flow between data and view.
# Linked Files:
# - Uses AdminMaterialSummaryData (Model) to fetch data.
# - Controls AdminMaterialSummaryView (View) to display or hide the summary.








from ADMIN_material_summary_data import AdminMaterialSummaryData
from ADMIN_material_summary_view import AdminMaterialSummaryView

class AdminMaterialSummaryController:
    def __init__(self, parent):
        self.data_model = AdminMaterialSummaryData()  # Data handler (Model)
        self.view = AdminMaterialSummaryView(parent) # Visual display (View)
        self.displayed = False # Track whether the summary is currently shown

    def toggle_display(self):
        # Show or hide the summary section when triggered
        if self.displayed:
            # Hide the view
            self.view.frame.pack_forget()
            self.displayed = False
        else:
            # Fetch material totals from the database
            material_data = self.data_model.get_material_totals()
            # Pass the data to the view for rendering
            self.view.render(material_data)
            # Show the view
            self.view.frame.pack(pady=10, fill="x")
            self.displayed = True
