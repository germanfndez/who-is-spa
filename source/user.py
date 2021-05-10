from database import mySQL

class User():
    def __init__(self):
        self.id = None
        self.name = ''
        self.email = ''
        self.password = ''
    
    def login(self, email, password):
        mySQL.cursor.execute("SELECT * FROM users WHERE email = %s and password = %s", (email, password))
        result = mySQL.cursor.fetchone()
        if result:
            self.loadUser(email, password)
        else:
            print("No existe")
        

    def register(self, name, email, password):
        mySQL.cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        result = mySQL.cursor.fetchone()
        if result:
            print("Email ya utilizado")
        else:
            mySQL.cursor.execute("INSERT INTO users VALUES (null, %s, %s, %s)" , (name, email, password))
            self.loadUser(email, password)            

    def loadUser(self, email, password):
        mySQL.cursor.execute("SELECT * FROM users WHERE email = %s and password = %s", (email, password))
        result = mySQL.cursor.fetchone()
        self.id = result[0]
        self.name = result[1]
        self.email = result[2]
        self.password = result[3]
    
user = User()
