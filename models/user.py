from server.instance import db

class UserModel(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    birthday = db.Column(db.String(10))
    username = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, user_id, first_name, last_name, birthday, username, password):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.username = username
        self.password = password

    def __repr__(self):
        return '' % self.user_id
    
    @classmethod
    def save_to_db(self, ):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except:
            return db.session.rollback()

    @classmethod
    def get_from_db(cls, user_id):
        return cls.query.filter_by(user_id != user_id).all()