from datetime import datetime, timedelta
from flask import Blueprint, request, current_app, jsonify
from src.models.cards import Cards
from src.middleware.auth import auth

bp_card = Blueprint('card', __name__)



@bp_card.route('/account/card', methods=['POST'])
@auth
def create_card(current_user):
    try:
        body = request.get_json()
        card_exist = Cards.query.filter_by(pan=body['pan']).first()
        if card_exist:
            return jsonify({
                'message': 'Cartao ja existe'
            }), 400
        card = Cards(person_id=current_user.id, title=body['title'], pan=body['pan'], 
                     expiry_mm=body['expiry_mm'], expiry_yyy=body['expiry_yyyy'], security_code=body['security_code'], date=datetime.now())
        current_app.db.session.add(card)
        current_app.db.session.commit()
        return jsonify({
            'message': 'okay'
        }), 200
    except Exception as e:
        print(e)
        return jsonify({
            'erro': 'erro inesperado'
        }), 500
    
@bp_card.route('/account/cards', methods=['GET'])
@auth
def get_cards(current_user):
    try:
        cards = Cards.query.filter_by(person_id=current_user.id)
        cards_json = [cards_obj.to_json() for cards_obj in cards]

        return jsonify(cards_json), 200
    except Exception as e:
        print(e)
        return jsonify({
            'erro': 'erro inesperado'
        }), 500