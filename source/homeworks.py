from database import mySQL

class Homeworks(): 
    def __init__(self, userId):
        mySQL.cursor.execute("SELECT * FROM users_works WHERE id_user", (userId))
        result = mySQL.cursor.fetchall()
        self.homeworks = result
            
