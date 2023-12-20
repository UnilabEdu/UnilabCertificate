from src.models.base import BaseModel
from src.extensions import db

from werkzeug.security import generate_password_hash, check_password_hash


class User(BaseModel):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, name, password):
        self.name = name
        self.password = generate_password_hash(password)

    def check_pass(self, password):
        return check_password_hash(self.password, password)