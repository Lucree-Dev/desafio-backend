from fastapi import APIRouter
from fastapi import Depends

from auth.auth import auth_wrapper
from schema import Transfer as TransferSchema

from db import SQLITE_DB
from db import Person
from db import Card
from db import BankStatement

from datetime import datetime

transfer = APIRouter()


@transfer.post("/transfer")
def make_transfer(transfer_schema: TransferSchema, username=Depends(auth_wrapper)):
    try:
        with SQLITE_DB.atomic():
            person = Person.select().where(Person.username == username).get()
            friend = Person.select().where(Person.user_id == transfer_schema.friend_id).get()
            card = Card.select().where(Card.card_id == transfer_schema.billing_card.card_id).get()

            BankStatement.create(
                user_id=person,
                friend_id=friend,
                value=transfer_schema.total_to_transfer,
                date=datetime.today().date(),
                from_card=card
            )
    except Exception as error:
        raise error
