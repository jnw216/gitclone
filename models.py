from app import db
from sqlalchemy.dialectics.postgresql import JSON

class Commit(db.Model):
        __tablename__ = 'commits'

        id = db.Column(db.Integer, primary_key=True)
        filename = db.Column(db.String())
        message = db.Column(db.String())

        def __init__(self, filename, message):
            self.filename = filename
            self.message = message

        def __repr__(self):
            return '<id {}>'.format(self.id)

            