import mysql.connector as mysql
from settings import *

class mySQLClass():

    def __init__(self):
        self.database = mysql.connect(
            host = DATABASE_HOST,
            user = DATABASE_USER,
            passwd = DATABASE_PASS,
            database = DATABASE_DATABASE
        )

        self.cursor = self.database.cursor(buffered=True)

        self.createTables()

    def createTables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INT(10) AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(40) NOT NULL,
                email VARCHAR(90) NOT NULL,
                password VARCHAR(30) NOT NULL
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users_works(
                id_user INT(10),
                id INT(10) AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(40) NOT NULL,
                description VARCHAR(90) NOT NULL,
                data_start VARCHAR(40) NOT NULL,
                data_end VARCHAR(40) NOT NULL
            )
        """)
    
    def insert(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass


    



mySQL = mySQLClass()
