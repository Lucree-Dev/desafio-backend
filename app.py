from flask import Flask, request, jsonify, make_response
from marshmallow import ValidationError
from schemas.account import UserSchema, CardSchema, FriendSchema
from server.instance import server, db, app


user_schema = UserSchema()
card_schema = CardSchema()
friend_schema = FriendSchema()

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

@app.route('/account/card', methods=['POST'])
def post_card():
    try:
        card_data = card_schema.load(request.get_json())
        card_data.save_to_db()
        card = card_schema.dump(card_data)
    

        return make_response(card, 200)
    except ValidationError as error:
        return error.messages, 422

@app.route('/account/friend', methods=['POST'])
def post_friend():
    try:
        friend_data = friend_schema.load(request.get_json())
        friend_data.save_to_db()
        friend = friend_schema.dump(friend_data)
        return make_response(friend, 200)
    except ValidationError as err:
        return make_response(err.messages, 422)

if __name__ == '__main__':
    db.init_app(app)
    server.run()