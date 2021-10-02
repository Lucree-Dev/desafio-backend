from server.instance import db

class CardModel(db.Model):
    __tablename__ = 'cards'
    user_id = db.Column(db.String)
    card_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    pan = db.Column(db.String(16))
    expiry_mm = db.Column(db.String(2))
    expiry_yyyy = db.Column(db.String(4))
    security_code = db.Column(db.String(3))
    date = db.Column(db.String(10))

    def __init__(self, user_id, card_id, title, pan, expiry_mm, expiry_yyyy, security_code, date):
        self.user_id = user_id
        self.card_id = card_id
        self.title = title
        self.pan = pan
        self.expiry_mm = expiry_mm
        self.expiry_yyyy = expiry_yyyy
        self.security_code = security_code
        self.date = date
        
    def __repr__(self):
        return '' % self.card_id
    
    @classmethod
    def save_to_db(self, ):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def get_from_db(cls, ):
        return cls.query.filter_by().all()