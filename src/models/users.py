from src.models.base import BaseModel
from src.extensions import db


class User(BaseModel):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    password = db.Column(db.String)

