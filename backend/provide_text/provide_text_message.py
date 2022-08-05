import json
import logging.config
from flask import Blueprint, request

from database.database import get_client

# Settings for logging
# logging.basicConfig(filename='./var/log/messages.log', encoding='utf-8', level=logging.INFO)
logging.config.fileConfig("./logging.ini", disable_existing_loggers=False)
# Get an instance of a specific named logger
logger = logging.getLogger("message")
error_logger = logging.getLogger(__name__)

provide_text_message_bp = Blueprint('provide_text_message', __name__)


@provide_text_message_bp.route('/message', methods=['POST'])
def provide_text_message():
    try:
        data = json.loads(request.data)
        # unique_identifier = data['unique_identifier']
        unique_code = data['unique_code']
        unique_identifier = data['unique_identifier']
        message = data['message']
        if get_client(unique_code, unique_identifier):
            logger.info(f'Client {unique_identifier} added new message: {message}')
            return {"status": "ok", "message": "Message added successfully"}
        else:
            return {"status": "error", "message": "Client code does not match client identifier"}
    except KeyError as key_error:
        error_logger.error(f'Error: {key_error} This key is not correct')
        return {"status": "error", "message": "Key is not correct"}
    except json.JSONDecodeError as decode_error:
        error_logger.error(f'Error: {decode_error}')
        return {"status": "error", "message": "json is not valid"}
