from datetime import datetime

from peewee import Model
from peewee import SqliteDatabase

from peewee import CharField
from peewee import DateField
from peewee import FloatField
from peewee import ForeignKeyField

SQLITE_DB = SqliteDatabase('digital_account.db')


class Person(Model):
    user_id = CharField(unique=True)
    first_name = CharField(max_length=40)
    last_name = CharField(max_length=40)
    birthday = CharField(max_length=10)
    username = CharField(unique=True)
    password = CharField()

    class Meta:
        database = SQLITE_DB


class Friends(Model):
    from_user = ForeignKeyField(Person, backref='person')
    to_user = ForeignKeyField(Person, backref='related_to')

    class Meta:
        database = SQLITE_DB

        indexes = (
            (('from_user', 'to_user'), True),
        )


class Card(Model):
    card_id = CharField()
    title = CharField(max_length=25)
    PAN = CharField(max_length=20)
    expiry_mm = CharField(max_length=2)
    expiry_yyyy = CharField(max_length=4)
    security_code = CharField(max_length=3)
    date = DateField(default=datetime.today().date())

    owner = ForeignKeyField(Person, backref='cards')

    class Meta:
        database = SQLITE_DB


class BankStatement(Model):
    user_id = ForeignKeyField(Person, backref="user")
    friend_id = ForeignKeyField(Person, backref="friend")
    value = FloatField()
    date = DateField(default=datetime.today().date())
    from_card = ForeignKeyField(Card, backref="card")

    class Meta:
        database = SQLITE_DB
