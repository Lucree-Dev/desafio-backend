from config import db

import datetime


class PersonCardInformation(db.Model):
    __tablename__ = "card-information"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.String(41),
        nullable=False,
    )

    date_created = db.Column(
        db.DateTime,
        default=datetime.datetime.now()
    )

    card_id = db.Column(
        db.String(100),
        nullable=False,
    )

    title = db.Column(
        db.String(40),
        nullable=False
    )

    pan = db.Column(
        db.String(16),
        nullable=False,
        unique=True,
    )

    expiry_mm = db.Column(
        db.String(2),
        nullable=False,

    )

    expiry_yyyy = db.Column(
        db.String(4),
        nullable=False
    )

    security_code = db.Column(
        db.String(3),
        nullable=False
    )

    date = db.Column(
        db.String(10),
        nullable=False
    )

    def __init__(self, card_id, title, pan, expiry_mm, expiry_yyyy, security_code, date, user_id):
        self.card_id = card_id
        self.title = title
        self.pan = pan
        self.expiry_mm = expiry_mm
        self.expiry_yyyy = expiry_yyyy
        self.security_code = security_code
        self.date = date
        self.user_id = user_id
