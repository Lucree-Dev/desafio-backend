import sqlalchemy
import uuid
from fastapi import HTTPException
from src.infra.sqlalchemy.config.database import engine
from src.domain.repositories.card_repository import ICardRepository


class CardRepository(ICardRepository):

    def __init__(self):
        self.connection = engine

    async def create(self, informations):
        try:
            card_id = uuid.uuid4()
            with self.connection.connect() as db_cursor:
                db_cursor.execute(sqlalchemy.text(f"""
                INSERT INTO cards (id, title, pan, expiry_mm, expiry_yyyy, security_code, date, owner_id) VALUES (
                    '{card_id}',
                    '{informations.get('title')}',
                    '{informations.get('pan')}',
                    '{informations.get('expiry_mm')}',
                    '{informations.get('expiry_yyyy')}',
                    '{informations.get('security_code')}',
                    '{informations.get('date')}',
                    '{informations.get('owner_id')}'
                )"""))
                informations.update({'card_id': card_id })

                return informations
        except sqlalchemy.exc.IntegrityError as error:
            return HTTPException(400, detail="Cartão já existe.")
    
    async def findByUserId(self, user_id: str):
        """Find by user id"""
        cards = []
        try:
            with self.connection.connect() as db_cursor:
                result = db_cursor.execute(sqlalchemy.text(
                    f"SELECT * FROM cards WHERE owner_id = '{user_id}'")).fetchall()

            if result:
                for user in result:
                    cards.append(user._asdict())

            return cards
        except Exception as error:
            return error