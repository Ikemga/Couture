# widgets/login.py
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class LoginScreen(BoxLayout):
    # On crée des propriétés pour stocker les valeurs des champs
    username = StringProperty('')
    password = StringProperty('')
    
    def login(self, username, password):
        """
        Cette méthode est appelée quand l'utilisateur clique sur le bouton "Login".
        Elle peut contenir la logique de vérification (ex: appel à une API, vérification en BDD).
        """
        self.username = username
        self.password = password
        
        # Ici, on va simplement afficher les valeurs pour l'exemple
        print(f"Tentative de connexion avec :")
        print(f"Username: {self.username}")
        print(f"Password: {self.password}")
        
        # Vous pouvez ajouter votre logique de vérification ici
        if self.username == "admin" and self.password == "password":
            print("Connexion réussie !")
            # Vous pouvez naviguer vers un autre écran ici
        else:
            print("Erreur de connexion : identifiants incorrects.")