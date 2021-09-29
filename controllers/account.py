from flask import request
from flask_restx import Resource

from models.user import UserModel
from schemas.account import *  

from server.instance import server

account_ns = server.account_ns
user_schema = UserSchema(many=True)

ITEM_NOT_FOUND = 'Not found'

class Account(Resource):

    def post_person():
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


