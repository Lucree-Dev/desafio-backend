from server.instance import db
from datetime import date

class TransferModel(db.Model):
    __tablename__ = 'transfers'
    transfer_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String)
    friend_id = db.Column(db.String)
    value = db.Column(db.Integer)
    card_id = db.Column(db.String)
    date = db.Column(db.String(10))

    def __init__(self, user_id, friend_id, value, card_id, date):
        self.user_id = user_id
        self.friend_id = friend_id
        self.value = value
        self.card_id = card_id
        self.date = date

    def __repr__(self, ):
        return '' % self.user_id

    def remodel(friend_data):
        friend_data['card_id'] = friend_data['billing_card']['card_id']
        friend_data['value'] = friend_data['total_to_transfer']
        friend_data['date'] = date.today().strftime("%d/%m/%Y")
        del friend_data['billing_card']
        del friend_data['total_to_transfer']
        return friend_data

    def save_to_db(self, ):
        db.session.add(self)
        db.session.commit()
