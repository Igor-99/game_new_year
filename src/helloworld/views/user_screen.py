# views/user_screen.py
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from ..viewmodels.theme_viewmodel import ThemeViewModel

class UserScreen:
    def __init__(self, main_window):
        self.main_window = main_window 
        self.status = 0
        
    
    def check_status (self, sta):
        print("Только когда нажата кнопка Click me!")
        if sta == 0:              
            print("жопа")
            self.status_button("#50C878",True,"Ебашь")
        elif sta == 1:
            print("Хер")
            self.status_button("#EB4C42",False,"Долбаеб")
        elif sta == 2:
            print ("Заебись")
            self.status_button("#3B4BC8",True,"Ебашь")

    def status_button(self,color, sost, text):
        print(text)
        self.voting_button.text = text
        self.voting_button.enabled = sost
        print(f"Состояние кнопки = {sost}")
        self.voting_button.style.background_color = color
        
    #def on_button_click(self, widget):
        # Изменяем статус кнопки на неактивный
        #self.voting_button.enabled = False
        #print("Кнопка была нажата и теперь неактивна.")       
            



   
    def voting_users(self, widget):
        print("Заебал")
        


    def show_user_screen(self):

        self.main_box = toga.Box(style=Pack(direction=COLUMN,))
        # Добавляем 4 метки
        label1 = toga.Label("1  Леша", style=Pack(padding=10))

        label2 = toga.Label("300 баллов", style=Pack(padding=10))

        label3 = toga.Label("Ебет ли Владимир Космоса в ванной во время дрочки?", style=Pack(padding=10))

        self.voting_button = toga.Button("100 пудов", on_press=self.voting_users,style=Pack(
        background_color="#595959",  # Цвет фона кнопки
        color="white",  # Цвет текста
        padding=10,  # Внутренние отступы
        font_size=40,  # Размер шрифта
        direction=ROW, 
        alignment='center',
        ))
        button_1 = toga.Button("Click me!", on_press=lambda widget: self.check_status(self.status), style=Pack(padding=10))


        # Добавляем метки в главный box
        self.main_box.add(label1)
        self.main_box.add(label2)
        self.main_box.add(label3)
        self.main_box.add(self.voting_button)
        self.main_box.add(button_1)


        
        


        

        self.main_window.content = self.main_box  

    def close_app(self, widget):
        # Закрываем главное окно приложения
        self.main_window.close()






