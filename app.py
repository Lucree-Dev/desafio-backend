from flask import Flask, Response
from src.person import bp_person
from src.cards import bp_card
from src.transfer import bp_transfer
from src.config.database import db, configure
from src.models.person import Person
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp_person)
    app.register_blueprint(bp_card)
    app.register_blueprint(bp_transfer)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['JWT_SECRET_KEY'] = '1d6d9cd2-825d-43ac-aefd-bd6425e73c40'
    configure(app)
    JWTManager(app)

    @app.before_first_request
    def create_tables():
        db.create_all()

    @app.after_request
    def after_request(response):

        return response
    return app



create_app()