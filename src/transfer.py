from datetime import datetime, timedelta
from flask import Blueprint, request, current_app, jsonify
from src.models.cards import Cards
from src.models.friends import Friends
from src.models.transfer import Transfer
from src.middleware.auth import auth
import jwt
from sqlalchemy import or_

bp_transfer = Blueprint('transfer', __name__)



@bp_transfer.route('/account/transfer', methods=['POST'])
@auth
def create_transfer(current_user):
    try:
        body = request.get_json()
        is_friend = Friends.query.filter(Friends.person_id==current_user.id , Friends.friend_id==body['friend_id']).first()
        if not is_friend:
            friend = Friends(person_id=current_user.id, friend_id=body['friend_id'])
            current_app.db.session.add(friend)
            current_app.db.session.commit()
      
        card = Cards.query.filter_by(id=body['billing_card']['card_id'], person_id=current_user.id).first()

        if not card:
            return jsonify({
            'message': 'Cartao nao encontrado'
            }), 400
        transfer = Transfer(person_id=current_user.id, friend_id=body['friend_id'], value=body['total_to_transfer'], 
                     date=datetime.now(), card_id=card.id)
        current_app.db.session.add(transfer)
        current_app.db.session.commit()
        return jsonify({
            'message': 'okay'
        }), 200
    except Exception as e:
        print(e)
        return jsonify({
            'erro': 'erro inesperado'
        }), 500

@bp_transfer.route('/account/bank-statement', methods=['GET'])
@auth
def get_transfer(current_user):
    try:
        transfer = Transfer.query.filter_by(person_id=current_user.id)

        transfer_json = [transfer_obj.to_json() for transfer_obj in transfer]

        return jsonify(transfer_json), 200
    except Exception as e:
        print(e)
        return jsonify({
            'erro': 'erro inesperado'
        }), 500
    
@bp_transfer.route('/account/bank-statement/<user_id>', methods=['GET'])
@auth
def get_transfer_user(current_user, user_id):
    try:
        transfer = Transfer.query.filter_by(person_id=current_user.id, friend_id=user_id)

        transfer_json = [transfer_obj.to_json() for transfer_obj in transfer]

        return jsonify(transfer_json), 200
    except Exception as e:
        print(e)
        return jsonify({
            'erro': 'erro inesperado'
        }), 500