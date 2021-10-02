from marshmallow_sqlalchemy import ModelSchema
from models.friends import FriendModel
from models.user import UserModel
from models.cards import CardModel
from marshmallow import fields
from server.instance import db

class UserSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = UserModel
        sqla_session = db.session       
        user_id = fields.Integer(required=True)
        first_name = fields.String(required=True)
        last_name = fields.String(required=True)
        birthday = fields.String(required=True)
        username = fields.String(required=True)
        password = fields.String(required=True)

class CardSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = CardModel
        sqla_session = db.session
        user_id = fields.String(required=True)
        card_id = fields.Integer(required=True)
        title = fields.String(required=True)
        pan = fields.String(required=True)
        expiry_mm = fields.String(required=True)
        expiry_yyyy = fields.String(required=True)
        security_code = fields.String(required=True)
        date = fields.String(required=True)

class FriendSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = FriendModel
        sqla_session = db.session
        friend_id = fields.String(required=True)
        user_id = fields.String(required=True)
        username = fields.String(required=True)