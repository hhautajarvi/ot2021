from entities.user import User
from database_connection import get_database_connection

class UserRepository:
    def __init__(self, connection):
        self.connection = connection

    def create_user(self, username, password):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Users (username, password) VALUES (?, ?)", (username, password))
        self.connection.commit()
        user = User(username, password)
        return user

    def find_user(self, username, password):
        cursor = self.connection.cursor()
        cursor.execute("SELECT username, password FROM Users WHERE username=? AND password=?", (username, password))
        name = cursor.fetchone()
        user = User(name[0], name[1])
        return user