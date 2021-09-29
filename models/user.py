from db import db

class UserModel(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    birthday = db.Column(db.String(10), nullable=False)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)