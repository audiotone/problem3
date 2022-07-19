import sqlite3
import logging.config

# Settings for logging
#FORMAT = '%(asctime)s %(name)s %(levelname)s:%(message)s'
#logging.basicConfig(filename='./var/log/sqlite.log', encoding='utf-8', level=logging.DEBUG, format=FORMAT)
logging.config.fileConfig("./logging.ini", disable_existing_loggers=False)
logger = logging.getLogger(__name__)


def ensure_connection(function):
    def inner(*args, **kwargs):
        with sqlite3.connect('./sqlite/clients.db') as connection:
            result = function(*args, connection=connection, **kwargs)
        return result

    return inner


def catch_error(function):
    def inner(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except sqlite3.DataError as data_error:
            logger.error(f'Error: {data_error}')
            raise data_error
        except sqlite3.OperationalError as operational_error:
            logger.error(f'Error: {operational_error}')
            raise operational_error
        except sqlite3.IntegrityError as integrity_error:
            logger.error(f'Error: {integrity_error}')
            raise integrity_error
        except sqlite3.InternalError as internal_error:
            logger.error(f'Error: {internal_error}')
            raise internal_error
        except sqlite3.ProgrammingError as programming_error:
            logger.error(f'Error: {programming_error}')
            raise programming_error
        except sqlite3.NotSupportedError as not_supported_error:
            logger.error(f'Error: {not_supported_error}')
            raise not_supported_error
    return inner


@catch_error
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


@catch_error
@ensure_connection
def get_client(unique_code, unique_identifier, connection) -> bool:
    '''
    :param unique_code:
    :param unique_identifier:
    :return: true if client exist or false if don't exist
    '''
    cursor = connection.cursor()
    unicode_code_query = cursor.execute('''
        SELECT unique_code from clients
        WHERE unique_identifier = ?
        ''', (unique_identifier,))
    connection.commit()
    record = cursor.fetchone()
    if record:
        if record[0] == unique_code:
            return True
    return False


@catch_error
@ensure_connection
def add_new_client_to_db(unique_identifier, unique_code, connection):
    '''
    The method adds a new client to the database
    :param connection:
    :param unique_code:
    :param unique_identifier: unique client ID
    :return:unique_code -
    '''
    cursor = connection.cursor()
    result = cursor.execute("""
        INSERT INTO clients
        (unique_identifier, unique_code)
        VALUES (?, ?);""", (unique_identifier, unique_code))
    connection.commit()


@catch_error
def add_new_message(unique_identifier, unique_code, message, connection) -> bool:
    '''
    The method writes the provided text message to a var file if client code is correct
    :param unique_identifier:
    :param unique_code:
    :param message:
    :return:
    '''
    pass
