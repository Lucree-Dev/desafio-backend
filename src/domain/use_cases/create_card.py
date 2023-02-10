

from src.schemas.Card import Card
from src.domain.repositories.card_repository import ICardRepository


class CreateCard:

    def __init__(self, respository: ICardRepository):
        self.respository = respository

    async def perform(self, card_informations: Card):
        card_id = await self.respository.create(card_informations)
        return card_id
