from flask import Flask
from os import path


class Config:
    app = Flask(__name__)
    BASE_DIRECTORY = path.abspath(path.dirname(__file__))
    IMAGES_PATH = path.join(BASE_DIRECTORY, "images")

    SECRET_KEY = "bcslwqerob.;1'1"
    JWT_SECRET_KEY = "qweqweqwh123123/;"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(BASE_DIRECTORY, "database.db")