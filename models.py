from server.instance import db
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash


class UserModel(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.String(), primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    birthday = db.Column(db.String(10))
    username = db.Column((db.String), unique=True)
    password = db.Column(db.String)

    def __init__(self, user_id, first_name, last_name, birthday, username, password):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.username = username
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '' % self.user_id
    
    def save_to_db(self, ):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except:
            return db.session.rollback()

class CardModel(db.Model):
    __tablename__ = 'cards'
    card_id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String)
    pan = db.Column(db.String(16), unique=True)
    expiry_mm = db.Column(db.String(2))
    expiry_yyyy = db.Column(db.String(4))
    security_code = db.Column(db.String(3))
    date = db.Column(db.String(10))

    def __init__(self, card_id, title, pan, expiry_mm, expiry_yyyy, security_code, date):
        self.card_id = card_id
        self.title = title
        self.pan = pan
        self.expiry_mm = expiry_mm
        self.expiry_yyyy = expiry_yyyy
        self.security_code = security_code
        self.date = date
        
    def __repr__(self):
        return '' % self.card_id
    
    def save_to_db(self, ):
        db.session.add(self)
        db.session.commit()
        return self

class FriendModel(db.Model):
    __tablename__ = "friends"
    user_id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String, unique=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    birthday = db.Column(db.String)

    def __init__(self, user_id, username, first_name, last_name, birthday):
        self.user_id = user_id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday

    def __repr__(self):
        return '' % self.user_id


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        return self

class TransferModel(db.Model):
    __tablename__ = 'transfers'
    transfer_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
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
