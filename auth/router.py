from fastapi import APIRouter
from fastapi import HTTPException
from auth.schema import AuthSchema

from db import SQLITE_DB
from db import Person

from auth.auth import jwt_encode

import bcrypt

token = APIRouter()


@token.post("/token")
def get_token(login: AuthSchema):
    username, password = login.username, login.password

    try:
        with SQLITE_DB.atomic():
            query = Person.select().where(Person.username == username)
            for person in query:
                if bcrypt.checkpw(bytes(password, "UTF-8"), bytes(person.password, "UTF-8")):
                    jwt_token = jwt_encode(user=username)
                    return dict(access_token=jwt_token, token_type="bearer")

    except Exception:
        raise HTTPException(status_code=401, detail="Problem when logging in")