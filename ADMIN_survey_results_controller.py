#ADMIN_survey_results_controller.py
# This controller manages the toggling and displaying of survey results.


from ADMIN_survey_data import AdminSurveyData
from ADMIN_survey_results_view import AdminSurveyResultsView

class AdminSurveyResultsController:
    def __init__(self, parent):
        self.data_model = AdminSurveyData()
        self.view = AdminSurveyResultsView(parent)
        self.displayed = False

    def toggle_display(self):
        # Shows or hides the survey results frame.
        if self.displayed:
            self.view.frame.pack_forget()
            self.displayed = False
        else:
            survey_data = self.data_model.get_all_survey_responses()
            self.view.render(survey_data)
            self.view.frame.pack(pady=10, fill="x")
            self.displayed = True
