# models/user_model.py

import os
import firebase_admin
from firebase_admin import credentials, db
from ..models.firebase_app import FirebaseApp

class UserModel:
    def __init__(self):
        self.ref_users = FirebaseApp().get_database_reference('users')
        self.ref_users = db.reference('users')

    def add_user(self, name):
        self.ref_users.push({'name': name, 'score': '0', 'hide': 0})

    def get_users(self):
        return self.ref_users.get()

    def is_user_exists(self, name):
        users = self.get_users()
        hidden_users = {user_id: user_data for user_id, user_data in users.items() if user_data['hide'] == 0}
        return any(user_data["name"] == name for user_data in hidden_users.values())