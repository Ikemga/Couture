from kivy.app import App

from kivy.uix.accordion import FloatLayout


class LoginLayut(FloatLayout):
    
    def login(self):
        nom = self.ids.username_input.text
        password = self.ids.password_input.text
        
        app = App.get_running_app()
        role = app.db.check(nom, password)
        
        if role:
            print(f"LoginLayutConnexion réussie pour {nom} en tant que {role}.")
            if role == 'admin':
                app.root.current = 'menu_screen'
            else:
                app.root.current = 'user_session'
        else:
            print(f"Veuillez vérifier vos informations.")
            # Afficher un message d'erreur à l'utilisateur
            
#class AdminScreen(Screen):
#    pass

#class UserScreen(Screen):
#    pass
