from src.domain.use_cases.list_cards import ListCards
from src.infra.sqlalchemy.card_repository import CardRepository


def make_list_cards():
    card_repository = CardRepository()
    list_cards = ListCards(card_repository)

    return {
        "list_cards": list_cards
    }