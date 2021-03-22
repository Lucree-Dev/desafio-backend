from fastapi import APIRouter
from fastapi import Depends

from auth.auth import auth_wrapper
from db import Card as CardORM
from db import Person as PersonORM
from db import SQLITE_DB
from schema import Card as CardSchema

card = APIRouter()


@card.post("/card")
def add_card_to(card_schema: CardSchema, username=Depends(auth_wrapper)):
    try:
        with SQLITE_DB.atomic():
            query = PersonORM.select().where(PersonORM.username == username)
            for person in query:
                CardORM.create(
                    card_id=card_schema.card_id,
                    title=card_schema.title,
                    PAN=card_schema.PAN,
                    expiry_mm=card_schema.expiry_mm,
                    expiry_yyyy=card_schema.expiry_yyyy,
                    security_code=card_schema.security_code,
                    date=card_schema.date,
                    owner=person
                )

    except Exception as error:
        raise error
    return dict(message="Card successfully registered")


@card.get("/cards")
def get_all_cards_by_person(username=Depends(auth_wrapper)):
    try:
        with SQLITE_DB.atomic():
            person = PersonORM.select().where(PersonORM.username == username).get()
            query = (CardORM
                     .select()
                     .where(CardORM.owner == person))
            cards = []
            for card_row in query:
                card_dict = {
                    "card_id": card_row.card_id,
                    "title": card_row.title,
                    "PAN": card_row.PAN,
                    "expiry_mm": card_row.expiry_mm,
                    "expiry_yyyy": card_row.expiry_yyyy,
                    "security_code": card_row.security_code,
                    "date": card_row.date
                }
                cards.append(card_dict)

            return cards
    except Exception as error:
        raise error
