import sqlite3


class ClientsDatabase:
    def __init__(self, database = "clients.sqlite"):
        self._db = database
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            cursor.execute("""
            PRAGMA foreign_keys=on;
            """)
            connection.commit()

            cursor.execute("""
            CREATE TABLE IF NOT EXIST messages (
            id INTEGER PRIMARY KEY,
            message TEXT NOT NULL
            );
            """)
            connection.commit()

            cursor.execute("""
            CREATE TABLE IF NOT EXIST clients (
            id INTEGER PRIMARY KEY,
            unique_identifier TEXT NOT NULL,
            unique_code TEXT NOT NULL,
            FOREIGN KEY (messages_id) REFERENCES messages(id)
            );
            """)
            connection.commit()

    def get_clients(self):
        '''
        The method outputs a list of clients
        '''
        pass

    def add_new_client(self, unique_identifier):
        '''
        The method adds a new client to the database
        :param unique_identifier: unique client ID
        :return:unique_code -
        '''
        pass

    def add_new_message(self, unique_identifier, unique_code, message) -> bool:
        '''
        The method writes the provided text message to a log file if client code is correct
        :param unique_identifier:
        :param unique_code:
        :param message:
        :return:
        '''
        pass

