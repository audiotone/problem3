from flask import Flask
from flask import request
from logging import getLogger
import json
import pprint
import random

from test import test_get_unique_code
from database import init_db, get_client, add_new_client_to_db, add_new_message

#Get an instance of a logger
logger = getLogger(__name__)

app = Flask(__name__)

@app.route('/', methods=['POST'])
def add_new_client():
    '''
    the function accepts a request to create a new client with unique code
    '''
    r = request.get_json()
    unique_identifier = r['unique_identifier']
    add_new_client_to_db(unique_identifier)
    return '200'


@app.route('/message', methods=['POST'])
def provide_text_message(message, unique_code, unique_identifier):
    if get_client(unique_code, unique_identifier):
        add_new_message(unique_identifier, unique_code, message)
        logger.info(f'{message}')
        return "ok"
    else:
        return "An error has occurred"


def main():
    print('Start app')
    #test_get_unique_code(add_new_client)
    #Connect to database
    init_db()
    logger.info('Database create')


if __name__ == '__main__':
    main()
    app.run(host='0.0.0.0', port=8000, debug=True)
