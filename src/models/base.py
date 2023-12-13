from src.extensions import db
from flask_login import UserMixin


class BaseModel(db.Model,UserMixin):

    __abstract__ = True

    def create(self, commit=True, flush=False):
        db.session.add(self)

        if commit:
            self.save()

        if flush:
            self.delete()

    def save(self):
        db.session.commit()

    def delete(self):
        db.session.remove(self)
        db.session.commit()
