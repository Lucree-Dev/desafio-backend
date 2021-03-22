import bcrypt
from fastapi import APIRouter
from fastapi import HTTPException
from peewee import IntegrityError

from db import Person as PersonORM
from db import SQLITE_DB
from schema import Person as PersonSchema

person = APIRouter()


@person.post("/person")
def receive_person(person_schema: PersonSchema):
    try:
        hashed_password = bcrypt.hashpw(bytes(person_schema.password, 'UTF-8'), bcrypt.gensalt())
        hashed_password = hashed_password.decode('UTF-8')

        with SQLITE_DB.atomic():
            PersonORM.create(
                user_id=person_schema.user_id,
                first_name=person_schema.first_name,
                last_name=person_schema.last_name,
                birthday=person_schema.birthday,
                username=person_schema.username,
                password=hashed_password,
            )
    except IntegrityError:
        raise HTTPException(status_code=401, detail="registered user: \'{}\'.".format(person_schema.username))
    else:
        return dict(message="registered successfully")
