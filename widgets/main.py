from kivy.app import App
from kivy.uix.layout import Layout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

from login import LoginLayut
from bd_manage import bd_manager

Builder.load_file('../views/login.kv')
#Builder.load_file('../views/menu.kv')

class MenuScreen(Screen):
    pass

class MainApp(App):
    def build(self):
        self.db = bd_manager()
        
        # Ajout d'utilisateurs pour le test (uniquement la première fois)
        # Vous devriez commenter ou supprimer ces lignes en production
        self.db.add_user("admin", "admin123", "admin")
        self.db.add_user("daouda", "daouda123", "user")
        self.db.add_user("marcelin", "marcelin123", "user")
        self.db.add_user("toto", "toto123", "user")
        self.db.add_user("inouss", "inouss123", "user")

        sm = LoginLayut()
        #sm.add_widget(LoginLayut(name='menuScreen'))
        #sm.add_widget(MenuScreen(name='menu_screen'))
        
        return sm

    def on_stop(self):
        self.db.close()

if __name__ == '__main__':
    app = MainApp()
    app.run()


