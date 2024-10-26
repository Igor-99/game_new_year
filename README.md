# Проект game_new_year

## Введение
Приложение созданное на основе "Своя игра". 

### Архитектура MVVM:
   - (__Model__): Теперь у нас есть отдельный класс User Model, который отвечает за взаимодействие с Firebase. Он содержит методы для добавления пользователя и проверки существования пользователя.
   - (__View__): В классе HelloWorld теперь используется User ViewModel для проверки и добавления пользователей. Это позволяет отделить логику от интерфейса.
   - (__ViewModel__): Класс User ViewModel управляет состоянием приложения и обрабатывает логику, связанную с пользователями.

### Язык программирования: 
   Python

### База данных:
   Firebase

### GUI:
   Beeware
   
## Структура проекта
```plaintext
helloworld/
├── src/
│   └── helloworld/
│       ├── __init__.py
│       ├── __main__.py
│       │
│       ├── models/
│       │   ├── __init__.py
│       │   ├── firebase_app.py
│       │   ├── theme_model.py
│       │   └── user_model.py
│       │
│       ├── viewmodels/
│       │   ├── __init__.py
│       │   ├── theme_viewmodel.py
│       │   └── user_viewmodel.py
│       │
│       └── views
│           ├── __init__.py
│           └── app.py
