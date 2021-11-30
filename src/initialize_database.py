from database_connection import get_database_connection

def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute('''
        DROP TABLE if exists Users;
    ''')
    cursor.execute('''
        DROP TABLE if exists Budget;
    ''')
    connection.commit()

def create_tables(connection):
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
            utilities INTEGER
        );
    ''')
    connection.commit()

def initialize_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)

if __name__ == '__main__':
    initialize_database()
