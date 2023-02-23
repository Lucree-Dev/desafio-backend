from flask_sqlalchemy import SQLAlchemy
from src.config.database import db


class Friends(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    person_id = db.Column(db.String(255))
    friend_id = db.Column(db.String(255))

    def to_json(self):
        return {
            "id": self.id,
            "person_id": self.person_id,
            "friend_id": self.title
        }