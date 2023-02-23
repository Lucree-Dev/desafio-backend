from functools import wraps
from flask import request, jsonify, current_app
import jwt
from src.models.person import Person
def auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        
        if not token:
            return jsonify({'message': 'Token nao encontrado'}), 401
        
        try:
            data = jwt.decode(
                token, current_app.config['JWT_SECRET_KEY'], algorithms="HS256"
            )
            current_user = Person.query.filter_by(id=data['id']).first()
        except Exception as e:
            print(e)
            return jsonify({
                'message': 'Token inválido'
            }), 401
        return f(current_user, *args, **kwargs)
    return decorated
