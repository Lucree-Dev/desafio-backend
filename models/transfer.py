from server.instance import db

class TransferModel(db.Model):
    __tablename__ = 'transfers'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String)
    friend_id = db.Column(db.String, primary_key=True)
    total_to_transfer = db.Column(db.Integer)
    billing_card_id = db.Column(db.String)
    date = db.Column(db.String(10))

    def __init__(self, user_id, friend_id,total_to_transfer, billing_card_id, date):
        self.user_id = user_id
        self.friend_id = friend_id
        self.total_to_transfer = total_to_transfer
        self.billing_card = billing_card_id
        self.date = date

    def __repr__(self, ):
        return f'TransferModel(user_id={self.user_id}, friend_id={self.friend_id}, total_to_transfer={self.total_to_transfer}, billing_card={self.billing_card_id}, date={self.date})'
    
    def jason(self, ):
        return {
            'user_id' : self.user_id,
            'friend_id' : self.friend_id,
            'total_to_transfer' : self.total_to_transfer,
            'billing_card' : self.billing_card_id,
            'date' : self.date
            }
    
    @classmethod
    def save_to_db(self, ):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_from_db(cls, ):
        return cls.query.filter_by().all()