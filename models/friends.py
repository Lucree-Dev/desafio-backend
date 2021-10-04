from server.instance import db

class FriendModel(db.Model):
    __tablename__ = "friends"
    user_id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String)
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