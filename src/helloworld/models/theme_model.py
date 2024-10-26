# models/theme_model.py

import os
import firebase_admin
from firebase_admin import credentials, db
from ..models.firebase_app import FirebaseApp

class ThemeModel:
    def __init__(self):
        self.ref_theme = FirebaseApp().get_database_reference('theme')
        self.ref_theme = db.reference('theme')

    def add_theme(self, answer, question, theme):
        self.ref_theme.push({'answer': answer, 'question': question, 'theme': theme, 'status': 0})

    def get_theme(self):
        return self.ref_theme.get()

    def get_name_theme_list(self):
        themes = self.ref_theme.get()
        self.theme_list_6 = [
            f"{themes['-O9hZ4gy8_-4QxMb54Gw']['theme']}",
            f"{themes['-O9hZ4yVN4u2PMuWwkJG']['theme']}",
            f"{themes['-O9hZ5DYfntJaQY5pO7p']['theme']}",
            f"{themes['-O9hZ5TOitUU2Vj2-r4L']['theme']}",
            f"{themes['-O9hZ5i1aNP-OJLCCgos']['theme']}",
            f"{themes['-O9hZ5xwKVEVfCqpvac9']['theme']}"
        ]
        return self.theme_list_6


    # def is_user_exists(self, name):
    #     users = self.get_users()
    #     hidden_users = {user_id: user_data for user_id, user_data in users.items() if user_data['hide'] == 0}
    #     return any(user_data["name"] == name for user_data in hidden_users.values())