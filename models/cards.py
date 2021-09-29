from db import db

class CardModel(db.Model):
    __tablename__ = 'cards'
    card_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    pan = db.Column(db.String(16), nullable=False)
    expiry_mm = db.Column(db.String(2), nullable=False)
    expiry_yyyy = db.Column(db.String(4), nullable=False)
    security_code = db.Column(db.String(3), nullable=False)
    date = db.Column(db.String(10), nullable=False)