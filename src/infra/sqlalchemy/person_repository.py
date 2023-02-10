
import sqlalchemy
from fastapi import HTTPException
import sqlalchemy.exc
from src.infra.sqlalchemy.config.database import engine
from src.domain.repositories.person_repository import IPersonRepository
import uuid


class PersonRepository(IPersonRepository):

    def __init__(self):
        self.connection = engine

    def create(self, informations: dict):
        """Create Person"""

        try:
            person_id = uuid.uuid4()
            with self.connection.connect() as db_cursor:
                db_cursor.execute(sqlalchemy.text(f"""
                INSERT INTO people (id, first_name, last_name, birthday, username, password) VALUES (
                    '{person_id}',
                    '{informations.get('first_name')}',
                    '{informations.get('last_name')}',
                    '{informations.get('birthday')}',
                    '{informations.get('username')}',
                    '{informations.get('password')}'
                )"""))
                pass_count = len(informations.get('password'))
                anonymize = '*' * pass_count
                informations.update({ 'password': anonymize})
                informations.update({'user_id': person_id })

                return informations
        except sqlalchemy.exc.IntegrityError:
            return HTTPException(400, detail="Username já existe.")

    def findAll(self):
        users = []
        try:
            with self.connection.connect() as db_cursor:
                result = db_cursor.execute(sqlalchemy.text(
                    'SELECT * FROM people')).fetchall()

            if result:
                for user in result:
                    users.append(user._asdict())

            return users
        except Exception as error:
            return error
