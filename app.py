from flask import Flask
from flask import request
import json
import pprint
import random

from test import test_get_unique_code
from database import ClientsDatabase

app = Flask(__name__)
db = ClientsDatabase()

@app.route('/', methods=['GET'])
def add_new_client(unique_identifier):
    '''
    the function accepts a request to create a new client with unique code
    '''
    return db.add_new_client(unique_identifier)


@app.route('/message', methods=['POST'])
def provide_text_message(message, unique_code, unique_identifier):
    if db.add_new_message(unique_identifier,unique_code,message):
        return "ok"
    else:
        return "An error has occurred"


test_get_unique_code(add_new_client)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
