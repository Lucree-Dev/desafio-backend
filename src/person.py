from datetime import datetime, timedelta
from flask import Blueprint, request, current_app, jsonify
import json
from src.models.person import Person

from src.models.friends import Friends
from sqlalchemy import or_
import jwt
from src.middleware.auth import auth

bp_person = Blueprint('person', __name__)


@bp_person.route('/account/person', methods=['POST'])
def create_person():
    body = request.get_json()
    try:
        person_exist = Person.query.filter_by(username=body['username']).first()
        if person_exist:
            return jsonify({
            'message': 'Usuario ja cadastrado'
        }), 400
        person = Person(first_name=body['first_name'], last_name=body['last_name'], 
                        birthday=body['birthday'], username=body['username'], password=body['password'])
        person.crypto_password()
        current_app.db.session.add(person)
        current_app.db.session.commit()
        return jsonify({
            'message': 'okay'
        }), 200
    except Exception as e:
        print(e)


@bp_person.route('/login', methods=['POST'])
def login():
    try:
        body = request.get_json()
        user = Person.query.filter_by(username=body['username']).first()
        
        if user and user.verify_password(body['password']):
            access_token = jwt.encode({
                'id': user.id,
                'exp': datetime.utcnow() + timedelta(weeks=1)
            }, current_app.config['JWT_SECRET_KEY'])

            return jsonify({
                'access_token': access_token.decode("utf-8") 
            }), 200
        
        return jsonify({
            'message': 'Credenciais invalidas'
        }), 401
    except Exception as e:
        print(e)

@bp_person.route('/account/friends', methods=['GET'])
@auth
def get_friends(current_user):
    try:
        friends = current_app.db.session.query(Person, Friends).filter(Person.id==Friends.friend_id).filter(Friends.person_id==current_user.id)

        result = [person.to_json() for person, _ in friends]

        return jsonify(result), 200

    except Exception as e:
        print(e)
