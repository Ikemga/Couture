import sqlite3


#db_name = "../db/couture_bd.db"
class bd_manager:
    """
    Classe pour gérer la connexion et les opérations sur une base de données SQLite.
    """
    def __init__(self, db_name="../db/couture_bd.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self.connect()
        self.create_tables()

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            print("Connexion à la base de données SQLite réussie.")
        except sqlite3.Error as e:
            print(f"Erreur de connexion : {e}")

    def create_tables(self):
        
        #Supprime la table si elle exi
        
        self.cursor.execute("DROP TABLE IF EXISTS utilisateurs")

        # Exemple de création de table
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS utilisateurs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                password TEXT UNIQUE,
                role TEXT NOT NULL DEFAULT 'user'
            );
        """)
        
        self.conn.commit()

    def add_user(self, nom, password, role='user'):
        self.cursor.execute("INSERT INTO utilisateurs (nom, password,role) VALUES (?, ?,?)", (nom, password,role))
        self.conn.commit()

    def get_users(self):
        self.cursor.execute("SELECT * FROM utilisateurs")
        return self.cursor.fetchall()

    def close(self):
        if self.conn:
            self.conn.close()
    
    def check(self, nom,password,role):
        """
      
        """
        self.cursor.execute("SELECT * FROM utilisateurs WHERE nom=? AND password=? AND role=?", (nom,password,role))
        user = self.cursor.fetchone()
        return user is not None