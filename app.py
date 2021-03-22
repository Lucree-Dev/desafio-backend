from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields, validates_schema, ValidationError
from datetime import date
# from sqlalchemy.sql import select ###11
from numpy import asarray
import json
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://<username>:<pass>@localhost:3306/<DB>'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:''@127.0.0.1/db_cartao'


db = SQLAlchemy(app)


# Model Card
class Card(db.Model):
    __tablename__ = "card"
    card_id = db.Column(db.String(45), primary_key=True)
    title = db.Column(db.String(45))
    pan = db.Column(db.String(45))
    expiry_mm = db.Column(db.String(45))
    expiry_yyyy = db.Column(db.String(45))
    security_code = db.Column(db.String(45))
    date = db.Column(db.String(45))
    user_id = db.Column(db.String(100))

    def create(self):

        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, card_id, title, pan, expiry_mm, expiry_yyyy, security_code, date, user_id):
        self.card_id = card_id
        self.title = title
        self.pan = pan
        self.expiry_mm = expiry_mm
        self.expiry_yyyy = expiry_yyyy
        self.security_code = security_code
        self.date = date
        self.user_id = user_id

    def __repr__(self):
        return '' % self.card_id

    def columns():
        return ['card_id', 'title', 'pan', 'expiry_mm', 'expiry_yyyy', 'security_code', 'date']


class CardSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Card
        sqla_session = db.session
        user_id = fields.String(required=True)
        card_id = fields.String(required=True)
        title = fields.String(required=True)
        pan = fields.String(required=True)
        expiry_mm = fields.String(required=True)
        expiry_yyyy = fields.String(required=True)
        security_code = fields.String(required=True)
        date = fields.String(required=True)


# Model Person
class Person(db.Model):
    __tablename__ = "person"
    user_id = db.Column(db.String(45), primary_key=True)
    username = db.Column(db.String(45))
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    birthday = db.Column(db.String(45))
    password = db.Column(db.String(45))
    # card_id =  db.Column(db.Integer, db.ForeignKey('card.card_id'))
    # card = db.relationship("Card")

    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except:
            return db.session.rollback()

    def __init__(self, user_id, username, first_name, last_name, birthday, password):
        self.user_id = user_id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.password = password

    def __repr__(self):
        return '' % self.user_id


class PersonSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Person
        sqla_session = db.session
        user_id = fields.String(required=True)
        username = fields.String(required=True)
        first_name = fields.String(required=True)
        last_name = fields.String(required=True)
        birthday = fields.String(required=True)
        password = fields.String(required=True)


# Model Friends
class Friend(db.Model):
    __tablename__ = "friends"
    friend_id = db.Column(db.String(45), primary_key=True)
    user_id = db.Column(db.String(45))
    username = db.Column(db.String(45))
    birthday = db.Column(db.String(45))
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, friend_id, user_id, username, birthday, first_name, last_name):
        self.friend_id = friend_id
        self.user_id = user_id
        self.username = username
        self.birthday = birthday
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return '' % self.user_id

    def columns():
        return ['first_name', 'last_name', 'birthday', 'username', 'user_id']


class FriendSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Friend
        sqla_session = db.session
        friend_id = fields.String(required=True)
        user_id = fields.String(required=True)
        username = fields.String(required=True)
        birthday = fields.String(required=True)
        first_name = fields.String(required=True)
        last_name = fields.String(required=True)

# Model Transfer


class Transfer(db.Model):
    __tablename__ = "transfer"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(45))
    friend_id = db.Column(db.String(45))
    value = db.Column(db.Integer)
    card_id = db.Column(db.String(45))
    date = db.Column(db.String(45))

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, user_id, friend_id, value, card_id, date):

        self.user_id = user_id
        self.friend_id = friend_id
        self.value = value
        self.card_id = card_id
        self.date = date

    def __repr__(self):
        return '' % self.user_id

    def set_data(data):
        data['card_id'] = data['billing_card']['card_id']
        data['value'] = data['total_to_transfer']
        data['date'] = date.today().strftime("%m/%d/%Y")
        del data['billing_card']
        del data['total_to_transfer']
        return data

    def columns():
        return ['user_id', 'friend_id', 'value', 'date', 'card_id']


class TransferSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Transfer
        sqla_session = db.session
        user_id = fields.String(required=True)
        friend_id = fields.String(required=True)
        value = fields.Integer(required=True)
        card_id = fields.String(required=True)
        date = fields.String(required=True)


@app.route('/cards', methods=['GET'])
def all_cards():
    get_cards = Card.query.all()
    cards_schema = CardSchema(many=True, only=Card.columns())
    cards = cards_schema.dump(get_cards)
    return make_response(jsonify(cards))


@app.route('/card/<id>', methods=['GET'])
def get_card_by_id(id):
    get_card = Card.query.get(id)
    if not get_card:
        return make_response({'error': 'ID não encontrado'}, 404)
    card_schema = CardSchema(only=Card.columns())
    card = card_schema.dump(get_card)
    return make_response(jsonify(card))


@app.route('/card/<id>', methods=['PUT'])
def update_card_by_id(id):
    data = request.get_json()
    get_card = Card.query.get(id)
    if data.get('title'):
        get_card.title = data['title']
    if data.get('pan'):
        get_card.pan = data['pan']
    if data.get('expiry_mm'):
        get_card.expiry_mm = data['expiry_mm']
    if data.get('expiry_yyyy'):
        get_card.expiry_yyyy = data['expiry_yyyy']
    if data.get('security_code'):
        get_card.security_code = data['security_code']
    if data.get('date'):
        get_card.date = data['date']
    db.session.add(get_card)
    db.session.commit()
    get_card_schema = CardSchema(
        only=['card_id', 'title', 'pan', 'expiry_mm', 'expiry_yyyy', 'date'])
    card = get_card_schema.dump(get_card)
    return make_response(jsonify(card))


@app.route('/card/<id>', methods=['DELETE'])
def delete_card_by_id(id):
    get_card = Card.query.get(id)
    if not get_card:
        return make_response({'error': 'ID não encontrado'}, 404)
    db.session.delete(get_card)
    db.session.commit()
    return make_response('', 204)


@app.route('/card', methods=['POST'])
def create_card():
    try:
        data = request.get_json()
        card_schema = CardSchema()
        card = card_schema.load(data)
        result = card_schema.dump(card.create())
        return make_response(result, 200)
    except ValidationError as err:
        return err.messages, 422


@app.route('/account/person', methods=['POST'])
def create_person():
    try:
        data = request.get_json()
        person_schema = PersonSchema()
        person = person_schema.load(data)
        result = person_schema.dump(person.create())
        return make_response(result, 200)
    except ValidationError as err:
        return make_response(err.messages, 422)


@app.route('/account/friend', methods=['POST'])
def create_friend():
    try:
        data = request.get_json()
        friend_schema = FriendSchema()
        friend = friend_schema.load(data)
        result = friend_schema.dump(friend.create())
        return make_response(result, 200)
    except ValidationError as err:
        return make_response(err.messages, 422)


@app.route('/account/friends', methods=['GET'])
def all_friends():
    get_friend = Friend.query.all()
    friend_schema = FriendSchema(many=True)
    friend = friend_schema.dump(get_friend)
    return make_response(jsonify(friend))


@app.route('/account/transfer', methods=['POST'])
def create_transfer():
    try:
        if not request.get_json() or not 'user_id' in request.get_json():
            return make_response({'error': {'messenger': 'user_id not found'}}, 400)
        data = request.get_json()
        Transfer.set_data(data)
        transfer_schema = TransferSchema()
        transfer = transfer_schema.load(data)
        result = transfer_schema.dump(transfer.create())
        return make_response(result, 200)
    except ValidationError as err:
        return make_response(err.messages, 422)


@app.route('/account/bank-statement', methods=['GET'])
def all_bank_statement():
    try:
        get_bank_statement = Transfer.query.all()

        transfer_schema = TransferSchema(many=True, only=Transfer.columns())
        bank_statement = transfer_schema.dump(get_bank_statement)
        array_result = asarray(bank_statement)

        for value in array_result:
            value['from_card'] = value['card_id']
            del value['card_id']

        list = array_result.tolist()
        return make_response(json.dumps(list), 200)
    except ValidationError as err:
        return make_response(err.messages, 422)


@app.route('/account/bank-statement/<user_id>', methods=['GET'])
def all_bank_statement_id(user_id):
    return make_response({'error': {'messenger': 'not found'}}, 400)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=False)
