from config import db

import datetime


class BankInformations(db.Model):
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

    friend_id = db.Column(
        db.String(41),
        nullable=False,
    )

    value = db.Column(
        db.Integer,
        nullable=False,
    )

    from_card = db.Column(
        db.String(100),
        nullable=False,
    )

    def __init__(self, user_id, friend_id, value, from_card):
        self.user_id = user_id
        self.friend_id = friend_id
        self.value = value
        self.from_card = from_card
