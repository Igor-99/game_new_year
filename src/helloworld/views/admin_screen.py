# views/admin_screen.py
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from ..viewmodels.theme_viewmodel import ThemeViewModel

class AdminScreen:
    def __init__(self, main_window):
        self.main_window = main_window  # Сохраняем ссылку на главное окно
        self.view_model_theme = ThemeViewModel()  # Инициализация view model для тем
        self.main_box = toga.Box(style=Pack(direction=COLUMN))  # Создаем основной контейнер
        self.build_buttons()

    def show_admin_screen(self):
        self.main_window.content = self.main_box  # Устанавливаем основной контейнер как содержимое окна
        self.label = toga.Label("Добро пожаловать в Admin Screen!", style=Pack(padding=10))
        self.main_box.add(self.label)  # Добавляем метку в основной контейнер

    def on_select(self, widget, selection):
        print(f"Selected: {selection}")

    def close_app(self, widget):
        # Закрываем главное окно приложения
        self.main_window.close()

    def build_buttons(self):
        button_box = toga.Box(style=Pack(direction=ROW, padding=5))

        participants_button = toga.Button("Участники", on_press=self.change_user)
        tasks_button = toga.Button("Задания", on_press=self.change_task)
        game_button = toga.Button("Игра", on_press=self.open_game)

        button_box.add(participants_button)
        button_box.add(tasks_button)
        button_box.add(game_button)

        self.main_box.add(button_box)

    def change_user(self, widget):
        self.label.text = "Создан новый файл!"

    def change_task(self, widget):
        self.label.text = "Файл открыт!"

    def open_game(self, widget):
        self.label.text = "Файл сохранён!"
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
