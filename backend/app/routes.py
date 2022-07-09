from modules.add_new_client import add_new_client_bp
from provide_text.provide_text_message import provide_text_message_bp


def route(app):
    app.register_blueprint(add_new_client_bp)
    app.register_blueprint(provide_text_message_bp)
