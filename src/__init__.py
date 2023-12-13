from flask import Flask

from src.config import Config
from src.extensions import db, jwt_manager
from src.api import api
from src.commands import init_db, api_test


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    reg_ext(app)

    reg_commands(app)

    return app


def reg_ext(app):

    # Flask-sqlalchemy
    db.init_app(app)

    # Flask-restful
    api.init_app(app)

    # Flask-JWT-extended
    jwt_manager.init_app(app)


def reg_commands(app):
    app.cli.add_command(init_db)
    app.cli.add_command(api_test)