from server.instance import db

class FriendModel(db.Model):
    __tablename__ = "friends"
    user_id = db.Column(db.String, primary_key=True)
    friend_id = db.Column(db.String)
    username = db.Column(db.String)

    def __init__(self, user_id, friend_id, username,):
        self.user_id = user_id
        self.friend_id = friend_id
        self.username = username

    def __repr__(self):
        return '' % self.user_id


    @classmethod
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        return self