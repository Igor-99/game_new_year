# viewmodels/theme_viewmodel.py

from ..models.theme_model import ThemeModel

class ThemeViewModel:
    def __init__(self):
        self.theme_model = ThemeModel()
        self.theme_answer = ""
        self.theme_question = ""
        self.theme_theme = ""

    def set_theme(self, answer, question, theme):
        self.theme_answer = answer
        self.theme_question = question
        self.theme_theme = theme

    def check_user(self):
        return self.user_model.is_user_exists(self.username)

    def add_theme(self):
        self.theme_model.add_theme(self.theme_answer, self.theme_question, self.theme_theme)

    def get_theme_list_6(self):
        theme_list_6 = self.theme_model.get_name_theme_list()
        return theme_list_6