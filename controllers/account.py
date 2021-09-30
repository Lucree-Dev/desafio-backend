from flask import request
from schemas.account import UserSchema, CardSchema
from models.user import UserModel
from models.cards import CardModel
from models.transfer import TransferModel

user_schema = UserSchema(many=True)
card_schema = CardSchema(many=True)
#transfer_schema = TransferSchema()

ITEM_NOT_FOUND = 'Not found'

class Account():

    def post_person(self, ):
        person_json = request.get_json()
        person_data = user_schema.load(person_json)

        person_data.save_to_db()

        return user_schema.dump(person_data), 201

    def get_friends(self, user_id):
        friends_data = UserModel.get_from_db(user_id), 200
        if friends_data:
            return user_schema.dump(friends_data)
        else:
            return { 'message': ITEM_NOT_FOUND}, 404

    def post_card(self, ):
        card_json = request.get_json()
        card_data = card_schema.load(card_json)

        card_data.save_to_db()

        return card_schema.dump(card_data), 201

    def get_cards(self, ):
        cards_data = CardModel.get_from_db(), 200
        if cards_data:
            return card_schema.dump(cards_data)
        else:
            return { 'message': ITEM_NOT_FOUND}, 404

    def post_transfer(self, ):
        transfer_json = request.get_json()
        transfer_data = transfer_schema.load(transfer_json)

        transfer_data.save_to_db()

        return transfer_schema.dump(transfer_data), 201

    def get_transfers(self, ):
        transfers_data = TransferModel.get_from_db(), 200
        if transfers_data:
            return transfer_schema.dump(transfers_data)
        else:
            return { 'message': ITEM_NOT_FOUND}, 404
            