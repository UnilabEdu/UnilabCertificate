from src.models.base import BaseModel
from src.extensions import db


class Signature(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    lecturer_name = db.Column(db.String)
    picture_name = db.Column(db.String)

