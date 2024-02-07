from src.models.base import BaseModel
from src.extensions import db


class Certificate(BaseModel):
    __tablename__ = "certificates"

    uuid = db.Column(db.String)
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    date = db.Column(db.Date)
    generate_date = db.Column(db.Date)
    type = db.Column(db.String)
    subject = db.Column(db.String)