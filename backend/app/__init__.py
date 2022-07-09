import os
from flask import Flask
from app.routes import route
from app.config import config, init_config

# from test import test_get_unique_code
from database.database import init_db


def create_flask_app():
    app = Flask(__name__)

    route(app)
    path = os.environ.get('CONFIG_PATH') if os.environ.get('CONFIG_PATH') else "./settings.ini"
    init_config(path)
    try:
        app.config.update(dict(
            SECRET_KEY=str(config['FLASK_APP']['FLASK_APP_SECRET_KEY'])
        ))
        init_db()
        print(f"\n\033[32m Server start with config :\n\033[32m {path}\n")
    except KeyError:
        print(f"\n\033[31m File {path} not found or incorrect")

    return app
