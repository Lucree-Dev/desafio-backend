from flask_sqlalchemy import SQLAlchemy
from src.config.database import db
from hashlib import sha256

class Transfer(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    person_id = db.Column(db.String(255))
    friend_id = db.Column(db.String(255))
    value = db.Column(db.Integer())
    date = db.Column(db.String(255))
    card_id = db.Column(db.String(255))

    def to_json(self):
        return {
            "id": self.id,
            "person_id": self.person_id,
            "friend_id": self.friend_id,
            "value": self.value,
            "date": self.date,
            "from_card": self.card_id
        }