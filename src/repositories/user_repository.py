from entities.user import User
from database_connection import get_database_connection

class UserRepository:
    def __init__(self, connection):
        self.connection = connection

    def create_user(self, user):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Users (username, password) VALUES (?, ?)", (user.username, user.password))
        self.connection.commit()
        return user

    def find_user(self, username, password):
        cursor = self.connection.cursor()
        cursor.execute("SELECT username, password FROM Users WHERE username=? AND password=?", (username, password))
        name = cursor.fetchone()
        return name