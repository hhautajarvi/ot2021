import sqlite3
from config import DATABASE_FILE_PATH

connection = sqlite3.connect(DATABASE_FILE_PATH)
connection.row_factory = sqlite3.Row


def get_database_connection():
    """Luo tietokantayhteyden Connection-olion

    Returns:
        Palauttaa tietokantayhteyden Connection-olion
    """
    return connection
