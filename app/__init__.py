from flask import Flask
from os import getenv
from config import config_selector
from app.configurations import database, commands, serialization
from app import views
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()


def create_app():

    app = Flask(__name__)

    config_type = getenv("FLASK_ENV")
    app.config.from_object(config_selector[config_type])
    commands.init_app(app)
    database.init_app(app)
    views.init_app(app)
    serialization.init_app(app)
    CORS(app)

    return app
