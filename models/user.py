from db import db

class UserModel(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    birthday = db.Column(db.String(10))
    username = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, first_name, last_name, birthday, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.username = username
        self.password = password

    def __repr__(self, ):
        return f'UserModel(first_name={self.first_name}, last_name={self.last_name}, birthday={self.birthday}, username={self.username}, password={self.password})'
    
    def jason(self, ):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birthday': self.birthday,
            'username': self.username,
            'password': self.password
            }
    
    @classmethod
    def save_to_db(self, ):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_from_db(cls, user_id):
        return cls.query.filter_by(user_id != user_id).all()