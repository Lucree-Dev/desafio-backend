from ma import ma
from models.user import UserModel
from models.cards import CardModel
from models.transfer import TransferModel

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True

class CardSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CardModel
        load_instance = True

#class TransferSchema(ma.SQLAlchemyAutoSchema):
#   class Meta:
#       model = TransferModel
#       load_instance = True