from db import db

class CardModel(db.Model):
    __tablename__ = 'cards'
    card_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    pan = db.Column(db.String(16))
    expiry_mm = db.Column(db.String(2))
    expiry_yyyy = db.Column(db.String(4))
    security_code = db.Column(db.String(3))
    date = db.Column(db.String(10))