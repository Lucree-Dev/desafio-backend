from src.domain.use_cases.create_card import CreateCard
from src.infra.sqlalchemy.card_repository import CardRepository


def make_create_card():
    card_repository = CardRepository()
    create_card = CreateCard(card_repository)

    return {
        "create_card": create_card
    }