from flask import Blueprint, request
from database.database import add_new_client_to_db, check_unique_identifier_in_db
from .check_unique_identifier import check_unique_identifier_type
from .generate_unique_code import generate_unique_code
import json
import logging.config

# Settings for logging
logging.config.fileConfig("./logging.ini", disable_existing_loggers=False)
logger = logging.getLogger(__name__)

add_new_client_bp = Blueprint('add_new_client', __name__)


@add_new_client_bp.route('/', methods=['POST'])
def add_new_client():
    '''
    the function accepts a request to create a new client with unique code
    '''

    try:
        data = json.loads(request.data)
        unique_identifier = data['unique_identifier']
    # except ValueError:
    #     return {"status": "error", "message": "no json sent"}
    except KeyError as key_error:
        logger.error(f'Error: {key_error}')
        return {"status": "error", "message": "Key is not correct", "unique_code": None}
    except json.JSONDecodeError as decode_error:
        logger.error(f'Error: {decode_error}')
        return {"status": "error", "message": "Json is not valid", "unique_code": None}

    # TODO Is this type checking realy needed?
    # if check_unique_identifier_type(unique_identifier):
    if check_unique_identifier_in_db(unique_identifier):
        return {"status": "error", "message": "This unique identifier already exists", "unique_code": None}
    else:
        unique_code = generate_unique_code()
        add_new_client_to_db(unique_identifier, unique_code)
        return {"status": "ok", "message": "Unique identifier successfully generated", "unique_code": unique_code}
        # return {"status": "error", "message": "unique identifier has not string format"}
