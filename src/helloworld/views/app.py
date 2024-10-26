# views/app.py

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from ..viewmodels.user_viewmodel import UserViewModel
from ..viewmodels.theme_viewmodel import ThemeViewModel

class HelloWorld(toga.App):
    def startup(self):
        self.view_model = UserViewModel()
        self.view_model_theme = ThemeViewModel()
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.show_login_screen()
        self.main_window.show()

    def show_login_screen(self):
        self.main_box = toga.Box(style=Pack(direction=COLUMN))

        name_label = toga.Label(
            "Введите своё имя: ",
            style=Pack(padding=(0, 5)),
        )
        self.name_input = toga.TextInput(style=Pack(flex=1), placeholder="Поле не должно быть пустым")
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
            self.show_admin_screen()
            return
        if self.name_input.value == 'tv':
            # self.show_admin_screen()
            return        
        self.view_model.set_username(self.name_input.value)

        if self.view_model.check_user():
            self.name_input.value = ''
            self.name_input.placeholder = 'Такое имя уже существует'
            return

        self.view_model.add_user()
        

    def show_admin_screen(self):
        self.main_box = toga.ScrollContainer(style=Pack(direction=COLUMN))
        content_box = toga.Box(style=Pack(direction=COLUMN))

        # Получаем список тем
        theme_list = self.view_model_theme.get_theme_list_6()

        # Добавляем метки для тем и соответствующие выпадающие списки
        for theme in theme_list:
            theme_label = toga.Label(theme, style=Pack(padding=(0, 5)))
            content_box.add(theme_label)

            # Создаем новый экземпляр Selection для каждой темы
            theme_select = toga.Selection(items=['100', '200', '300', '400', '500'], on_select=self.on_select)
            content_box.add(theme_select)

        logout_button = toga.Button("Выйти", on_press=self.close_app, style=Pack(padding=5))
        content_box.add(logout_button)

        # Устанавливаем content_box как содержимое ScrollContainer
        self.main_box.content = content_box
        # Устанавливаем ScrollContainer как содержимое главного окна
        self.main_window.content = self.main_box


    def on_select(self, widget, selection):
        print(f"Selected: {selection}")
    def close_app(self, widget):
        # Закрываем главное окно приложения
        self.main_window.close()

def main():
    return HelloWorld()



        
        

        