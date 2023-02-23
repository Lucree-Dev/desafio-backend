from flask_sqlalchemy import SQLAlchemy
from src.config.database import db


class Cards(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    person_id = db.Column(db.String(255))
    title = db.Column(db.String(255))
    pan = db.Column(db.String(255))
    expiry_mm = db.Column(db.String(2))
    expiry_yyy = db.Column(db.String(4))
    security_code = db.Column(db.String(255))
    date = db.Column(db.String(11))

    def to_json(self):
        return {
            "id": self.id,
            "person_id": self.person_id,
            "title": self.title,
            "pan": self.pan,
            "expiry_mm": self.expiry_mm,
            "expiry_yyy": self.expiry_yyy,
            "date": self.date
        }