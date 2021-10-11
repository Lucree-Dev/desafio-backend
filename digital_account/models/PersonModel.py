from config import db

import datetime


class PersonInfoAccount(db.Model):
    __tablename__ = "person-info-account"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    date_created = db.Column(
        db.DateTime,
        default=datetime.datetime.now()
    )

    first_name = db.Column(
        db.String(64),
        nullable=False,
    )

    last_name = db.Column(
        db.String(99),
        nullable=False,
    )

    birthday = db.Column(
        db.String(40),
        nullable=False,
    )

    password = db.Column(
        db.String(40),
        nullable=False,
    )

    username = db.Column(
        db.String(40),
        unique=True,
        nullable=False,
    )

    user_id = db.Column(
        db.String(41),
        unique=True,
        nullable=False,
    )

    def __init__(self, first_name, last_name, birthday, password, username, user_id):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.password = password
        self.username = username
        self.user_id = user_id




