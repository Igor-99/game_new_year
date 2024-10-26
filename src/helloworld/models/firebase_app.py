import os, firebase_admin
from firebase_admin import credentials, db

class FirebaseApp:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            # Инициализация приложения Firebase
            cred = credentials.Certificate('D:/python_project/beeware/helloworld/src/helloworld/game-new-year-firebase.json')
            firebase_admin.initialize_app(cred, {'databaseURL': 'https://game-new-year-default-rtdb.firebaseio.com/'})
            cls._instance = super(FirebaseApp, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def get_database_reference(reference_path):
        return db.reference(reference_path)