from flask import Blueprint, request
from database.database import add_new_client_to_db
from .check_unique_identifier import check_unique_identifier_type
from .generate_unique_code import generate_unique_code
import json

add_new_client_bp = Blueprint('add_new_client', __name__)


@add_new_client_bp.route('/', methods=['POST'])
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
    if check_unique_identifier_type(unique_identifier):
        unique_code = generate_unique_code()
        add_new_client_to_db(unique_identifier, unique_code)
        return {"unique_code": unique_code}
    else:
        return {"status": "error", "message": "no string format"}
