from entities.user import User
from database_connection import get_database_connection

class UserRepository:
    def __init__(self, connection):
        self.connection = connection

    def create_user(self, username, password):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Users (username, password) VALUES (?, ?)", (username, password))
        self.connection.commit()
        user = User(cursor.lastrowid, username, password)
        return user

    def find_user(self, username):
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, username, password FROM Users WHERE username=?", \
            (username, ))
        name = cursor.fetchone()
        if name is None:
            return None
        return User(name[0], name[1], name[2])

    def delete_all(self):
        cursor = self.connection.cursor()
        cursor.execute("DELETE from Users")
        self.connection.commit()

user_repository = UserRepository(get_database_connection())
