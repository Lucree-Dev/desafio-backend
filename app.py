from flask import request
from ma import ma
from db import db
from controllers.account import Account
from server.instance import server

app = server.app
account_controller = Account()

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/account', methods=['POST'])
def post_person_route():
    request_body = request.json
    return account_controller.post_person()

@app.route('/account', methods=['GET'])
def get_friends_route(user_id):
    return account_controller.get_friends(user_id)

@app.route('/account', methods=['POST'])
def post_card_route():
    request_body = request.json
    return account_controller.post_card()

@app.route('/account', methods=['GET'])
def get_cards_route():
    return account_controller.get_cards()

@app.route('/account', methods=['POST'])
def post_transfer_route():
    request_body = request.json
    return account_controller.post_transfer()

@app.route('/account', methods=['GET'])
def get_tranfers_route():
    return account_controller.get_transfers()

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    server.run()