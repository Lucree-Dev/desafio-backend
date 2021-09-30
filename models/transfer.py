from db import db
from models.cards import CardModel

class TransferModel(db.Model):
    __tablename__ = 'transfers'
    friend_id = db.Column(db.String, primary_key=True)
    total_to_transfer = db.Column(db.Integer)
    billing_card = db.Column(#CardModel.card_id
    )

    def __init__(self, friend_id,total_to_transfer, billing_card):
        self.friend_id = friend_id
        self.total_to_transfer = total_to_transfer
        self.billing_card = billing_card

    def __repr__(self, ):
        return f'TransferModel(friend_id={self.friend_id}, total_to_transfer={self.total_to_transfer}, billing_card={self.billing_card})'
    
    def jason(self, ):
        return {
            'friend_id' : self.friend_id,
            'total_to_transfer' : self.total_to_transfer,
            'billing_card' : self.billing_card
            }
    
    @classmethod
    def save_to_db(self, ):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_from_db(cls, ):
        return cls.query.filter_by().all()