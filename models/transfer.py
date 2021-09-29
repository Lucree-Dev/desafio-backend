from db import db
from cards import CardModel

class TransferModel(db.Model):
    __tablename__ = 'transfers'
    friend_id = db.Column(db.String, primary_key=True)
    total_to_transfer = db.Column(db.Integer)
    billing_card = db.Column(CardModel.card_id)
