import json
import logging
from flask import Blueprint, request

from database.database import get_client

# Settings for logging
logging.basicConfig(filename='./var/log/messages.var', encoding='utf-8', level=logging.INFO)

provide_text_message_bp = Blueprint('provide_text_message', __name__)


@provide_text_message_bp.route('/message', methods=['POST'])
def provide_text_message():
    data = json.loads(request.data)
    # unique_identifier = data['unique_identifier']
    unique_code = data['unique_code']
    unique_identifier = data['unique_identifier']
    message = data['message']
    if get_client(unique_code, unique_identifier):
        logging.info(f'Client {unique_identifier} added new message: {message}')
        return {"status": "ok"}
    else:
        return {"status": "error", "message": "client code does not match client identifier"}
