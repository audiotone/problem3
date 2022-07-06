from flask import Flask
from flask import request
import logging
import json


from test import test_get_unique_code
from database import init_db, get_client, add_new_client_to_db
from service import generate_unique_code, unique_identifier_type_check

#Settings for logging
logging.basicConfig(filename='./backend/log/messages.log', encoding='utf-8', level=logging.INFO)


app = Flask(__name__)

@app.route('/', methods=['POST'])
def add_new_client():
    '''
    the function accepts a request to create a new client with unique code
    '''

    try:
        data = json.loads(request.data)
        unique_identifier = data['unique_identifier']
    except ValueError:
        return {"status": "error", "message": "no json sent"}
    except KeyError:
        return {"status": "error", "message": "key is not correct"}
    if unique_identifier_type_check(unique_identifier):
        unique_code = generate_unique_code()
        add_new_client_to_db(unique_identifier, unique_code)
        return {"unique_code": unique_code}
    else:
        return {"status": "error", "message": "no string format"}


@app.route('/message', methods=['POST'])
def provide_text_message():
    data = json.loads(request.data)
    unique_identifier = data['unique_identifier']
    unique_code = data['unique_code']
    unique_identifier = data['unique_identifier']
    message = data['message']
    if get_client(unique_code, unique_identifier):
        logging.info(f'Client {unique_identifier} added new message: {message}')
        return {"status": "ok"}
    else:
        return {"status": "error", "message": "client code does not match client identifier"}


def main():
    print('Start app')
    #test_get_unique_code(add_new_client)
    #Connect to database
    init_db()


if __name__ == '__main__':
    main()
    app.run(host='0.0.0.0', port=8000, debug=True)
