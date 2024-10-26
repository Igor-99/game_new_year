# views/app.py

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from ..viewmodels.user_viewmodel import UserViewModel
from ..viewmodels.theme_viewmodel import ThemeViewModel
from .admin_screen import AdminScreen
from .user_screen import UserScreen

class HelloWorld(toga.App):
    def startup(self):
        self.view_model = UserViewModel()
        self.view_model_theme = ThemeViewModel() 
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.show_login_screen()
        self.main_window.show()
        self.admin_screen = AdminScreen(self.main_window) 
        self.user_screen = UserScreen(self.main_window)

    def show_login_screen(self):
        self.main_box = toga.Box(style=Pack(direction=COLUMN))

        name_label = toga.Label(
            "Введите своё имя: ",
            style=Pack(padding=(0, 5)),
        )
        self.name_input = toga.TextInput(value = "test", style=Pack(flex=1), placeholder="Поле не должно быть пустым")
        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)

        button = toga.Button(
            "Вход",
            on_press=self.check_in_login,
            style=Pack(padding=5),
        )

        self.main_box.add(name_box)
        self.main_box.add(button)

        self.main_window.content = self.main_box  
    def check_in_login(self, widget):
        if self.name_input.value == '':
            self.name_input.placeholder = 'Заполните поле'
            return
        if self.name_input.value == 'ad':
            # self.admin_screen.show_admin_screen()
            return
        if self.name_input.value == 'tv':
            # self.show_admin_screen()
            return
        if self.name_input.value == 'test':
            self.user_screen.show_user_screen()
            return        
        self.view_model.set_username(self.name_input.value)

        if self.view_model.check_user():
            self.name_input.value = ''
            self.name_input.placeholder = 'Такое имя уже существует'
            return

        self.view_model.add_user()


def main():
    return HelloWorld()



        
        

        