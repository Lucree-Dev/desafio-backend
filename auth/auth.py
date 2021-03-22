from datetime import datetime
from datetime import timedelta

from fastapi import HTTPException
from fastapi import Security
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security import HTTPBearer
from jose import jwt

SECRET_KEY = "74951a1a8e4a567baeb2c1e03103f0b0a3703ec7846ef70fb403578e42a6c695"
ACCESS_TOKEN_EXPIRE_MINUTES = 15  # 64800  # 45 dias.

security = HTTPBearer()


def jwt_encode(user: str):
    payload = {
        'exp': datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
        'iat': datetime.utcnow(),
        'sub': user
    }

    return jwt.encode(claims=payload, key=SECRET_KEY)


def jwt_decode(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, ['HS256'])
        return payload['sub']
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Signature has expired')
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail='Invalid token')


def auth_wrapper(auth: HTTPAuthorizationCredentials = Security(security)):
    return jwt_decode(auth.credentials)
