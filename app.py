from flask import Flask
from flask import request
from logging import getLogger
import json
import pprint
import random

from test import test_get_unique_code
from database import init_db, get_client, add_new_client_to_db, add_new_message
from service import generate_unique_code, unique_identifier_type_check

#Get an instance of a logger
logger = getLogger(__name__)

app = Flask(__name__)

@app.route('/', methods=['POST'])
def add_new_client():
    '''
    the function accepts a request to create a new client with unique code
    '''

    try:
        data = json.loads(request.data)
    except ValueError:
        return {"status": "error", "message": "no json sent"}
    unique_identifier = data['unique_identifier']
    if unique_identifier_type_check(unique_identifier):
        unique_code = generate_unique_code()
        add_new_client_to_db(unique_identifier, unique_code)
        return {"unique_code": unique_code}
    else:
        return {"status": "error", "message": "no string format"}


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
