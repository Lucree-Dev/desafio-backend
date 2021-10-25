from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy

class Server():
    def __init__(self, ):
        self.app = Flask(__name__)
        self.blueprint = Blueprint('api', __name__, url_prefix='/api')
        self.app.register_blueprint(self.blueprint)
        
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
        self.app.config['PROPAGATE_EXCEPTIONS'] = True
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


    def run(self, ):
        self.app.run(
            port=5000,
            debug=True,
            host='0.0.0.0'
            )
server = Server()
app = server.app
db = SQLAlchemy(app)