from flask import Flask
from os import path


class Config():
    app = Flask(__name__)
    BASE_DIRECTORY = path.abspath(path.dirname(__file__))

    SECRET_KEY = "bcslwqerob.;1'1"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(BASE_DIRECTORY, "models/database.db")




