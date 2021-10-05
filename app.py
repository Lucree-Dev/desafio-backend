from flask import request, jsonify, make_response
from marshmallow import ValidationError
from models import FriendModel, CardModel, TransferModel
from schemas import UserSchema, CardSchema, FriendSchema, TransferSchema
from server.instance import server, db, app
import numpy as np
import json

user_schema = UserSchema()
card_schema = CardSchema()
friend_schema = FriendSchema()
transfer_schema = TransferSchema()

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/account/person', methods=['POST'])
def post_person():
    try:
        person_data = user_schema.load(request.get_json())
        person_data.save_to_db()
        person = user_schema.dump(person_data)
    
        return make_response(person, 200)
    except ValidationError as error:
        return make_response(error.messages, 422)

@app.route('/account/friend', methods=['GET'])
def get_friends():
    get_friends = FriendModel.query.all()
    friend_schema = FriendSchema(many=True)
    friends = friend_schema.dump(get_friends)
    return make_response(jsonify(friends))

@app.route('/account/card', methods=['POST'])
def post_card():
    try:
        card_data = card_schema.load(request.get_json())
        card_data.save_to_db()
        card = card_schema.dump(card_data)

        return make_response(card, 200)
    except ValidationError as error:
        return error.messages, 422

@app.route('/account/cards', methods=['GET'])
def get_cards():
    try:
        get_cards = CardModel.query.all()
        card_schema = CardSchema(many=True)
        cards = card_schema.dump(get_cards)
        return make_response(jsonify(cards))  
    except ValidationError as error:
        return error.messages, 422

@app.route('/account/friend', methods=['POST'])
def post_friend():
    try:
        friend_data = friend_schema.load(request.get_json())
        friend_data.save_to_db()
        friend = friend_schema.dump(friend_data)
        return make_response(friend, 200)
    except ValidationError as error:
        return make_response(error.messages, 422)

@app.route('/account/transfer', methods=['POST'])
def post_transfer():
    try:
        transfer_data = request.get_json()
        TransferModel.remodel(transfer_data)
        transfer = transfer_schema.load(transfer_data)
        transfer.save_to_db()
        transfer = transfer_schema.dump(transfer_data)
        return make_response(transfer, 200)
    except ValidationError as error:
        return make_response(error.messages, 422)

@app.route('/account/bank-statement', methods=['GET'])
def get_bank_statement():
    try:
        bank_statement = TransferModel.query.all()
        transfer_schema = TransferSchema(many=True)
        bank_statement = transfer_schema.dump(bank_statement)
        array = np.asarray(bank_statement)
        lst = array.tolist()
        return make_response(json.dumps(lst), 200)
    except ValidationError as error:
        return make_response(error.messages, 422)

@app.route('/account/bank-statement/<user_id>', methods=['GET'])
def get_bank_statement_id(user_id):
    try:    
        bank_statement = TransferModel.query.filter_by(user_id=user_id).all()
        transfer_schema = TransferSchema(many=True)
        bank_statement = transfer_schema.dump(bank_statement)
        array_result = np.asarray(bank_statement)
        lst = array_result.tolist()
        return make_response(json.dumps(lst), 200)
    except ValidationError as error:
        return make_response(error.messages, 422)

if __name__ == '__main__':
    db.init_app(app)
    server.run()