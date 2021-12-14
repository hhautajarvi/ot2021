from database_connection import get_database_connection

def drop_tables(connection):
    """Poistaa tietokantataulut

    Args:
        connection: Tietokantayhteyden Connection-olio
    """
    cursor = connection.cursor()
    cursor.execute('''
        DROP TABLE if exists Users;
    ''')
    cursor.execute('''
        DROP TABLE if exists Budget;
    ''')
    cursor.execute('''
        DROP TABLE if exists Expense;
    ''')
    connection.commit()

def create_tables(connection):
    """Luo tietokantataulut

    Args:
        connection: Tietokantayhteyden Connection-olio
    """
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE Users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT
        );
    ''')
    cursor.execute('''
        CREATE TABLE Budget(
            id INTEGER PRIMARY KEY,
            user_id INTEGER REFERENCES Users,
            amount INTEGER,
            food INTEGER,
            transit INTEGER,
            entertainment INTEGER,
            living INTEGER,
            utilities INTEGER,
            insurance INTEGER
        );
    ''')
    cursor.execute('''
        CREATE TABLE Expense(
            id INTEGER PRIMARY KEY,
            user_id INTEGER REFERENCES Users,
            amount INTEGER,
            category INTEGER,
            comment TEXT,
            date DATE
        );
    ''')
    connection.commit()

def initialize_database():
    """Alustaa tietokantataulut
    """
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)

if __name__ == '__main__':
    initialize_database()
