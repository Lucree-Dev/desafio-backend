from flask_sqlalchemy import SQLAlchemy
from src.config.database import db
from hashlib import sha256

class Person(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    birthday = db.Column(db.String(255))
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def crypto_password(self):
        self.password = sha256(self.password.encode('utf-8')).hexdigest()
    
    def verify_password(self, password):
        return sha256(password.encode('utf-8')).hexdigest() == self.password

    def to_json(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birthday": self.birthday,
            "username": self.username,
            "password": self.password
        }