# views/user_screen.py
import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from ..viewmodels.theme_viewmodel import ThemeViewModel

class UserScreen:
    def __init__(self, main_window):
        self.main_window = main_window  


    def show_user_screen(self):
        self.main_box = toga.Box(style=Pack(direction=COLUMN))
        self.main_window.content = self.main_box  

    def close_app(self, widget):
        # Закрываем главное окно приложения
        self.main_window.close()