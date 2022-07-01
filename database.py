import sqlite3

def ensure_connection(function):
    def inner(*args, **kwargs):
        with sqlite3.connect('clients.db') as connection:
            result = function(*args, connection=connection, **kwargs)
        return result
    return inner


@ensure_connection
def init_db(connection):
    cursor = connection.cursor()
    cursor.execute("""
        PRAGMA foreign_keys=on;
        """)
    connection.commit()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        message TEXT,
        client_id INTEGER NOT NULL,
        FOREIGN KEY (client_id) REFERENCES clients(id)
        )
        """)
    connection.commit()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clients(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        unique_identifier TEXT NOT NULL,
        unique_code TEXT NOT NULL
        );
        """)
    connection.commit()





@ensure_connection
def get_client(unique_code, unique_identifier, connection) -> bool:
    '''
    :param unique_code:
    :param unique_identifier:
    :return: true if client exist or false if don't exist
    '''
    cursor = connection.cursor()
    cursor.execute('''
        SELECT from clients id
        WHERE (unique_code==unique_code, unique_identifier==unique_identifier)
        ''')
    connection.commit()


@ensure_connection
def add_new_client_to_db(unique_identifier, connection):
    '''
    The method adds a new client to the database
    :param unique_identifier: unique client ID
    :return:unique_code -
    '''
    cursor = connection.cursor()
    result = cursor.execute("""
        INSERT INTO clients
        (unique_identifier, unique_code)
        VALUES (?, random());""", (unique_identifier,))
    connection.commit()


def add_new_message(unique_identifier, unique_code, message, connection) -> bool:
    '''
    The method writes the provided text message to a log file if client code is correct
    :param unique_identifier:
    :param unique_code:
    :param message:
    :return:
    '''
    pass



