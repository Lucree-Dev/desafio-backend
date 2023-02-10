import uuid
import sqlalchemy
from fastapi import HTTPException
from src.infra.sqlalchemy.config.database import engine
from src.domain.repositories.transfer_repository import ITransferRepository

class TransferRepository(ITransferRepository):

    def __init__(self):
        self.connection = engine

    async def create(self, informations):
        try:
            transfer_id = uuid.uuid4()
            with self.connection.connect() as db_cursor:
                db_cursor.execute(sqlalchemy.text(f"""
                INSERT INTO transfers (id, friend_id, total_to_transfer, billing_card) VALUES (
                    '{transfer_id}',
                    '{informations.get('friend_id')}',
                    '{informations.get('total_to_transfer')}',
                    '{informations.get('billing_card').get('card_id')}'
                )"""))

                return informations
        except sqlalchemy.exc.IntegrityError as error:
            print(error)
            return HTTPException(400, detail="Cartão já existe.")