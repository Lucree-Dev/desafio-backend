from fastapi import APIRouter
from src.schemas.Card import Card
from src.factories.create_card_factory import make_create_card
from src.factories.list_cards_factory import make_list_cards

cards = APIRouter()

@cards.get('/account/cards/{user_id}')
async def list_cards_controller(user_id: str):
    print(user_id)
    list_cards = make_list_cards().get('list_cards')
    cards = await list_cards.perform({"user_id": user_id})

    return cards

@cards.post('/account/card')
async def create_card_controller(card_informations: Card):
    create_card = make_create_card().get('create_card')
    card = await create_card.perform({
        "title": card_informations.title,
        "pan": card_informations.pan,
        "expiry_mm": card_informations.expiry_mm,
        "expiry_yyyy": card_informations.expiry_yyyy,
        "security_code": card_informations.security_code,
        "date": card_informations.date,
        "owner_id": card_informations.owner_id
    })
    
    return card