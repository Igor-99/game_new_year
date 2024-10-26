# viewmodels/user_viewmodel.py

from ..models.user_model import UserModel

class UserViewModel:
    def __init__(self):
        self.user_model = UserModel()
        self.username = ""

    def set_username(self, name):
        self.username = name

    def check_user(self):
        return self.user_model.is_user_exists(self.username)

    def add_user(self):
        self.user_model.add_user(self.username)