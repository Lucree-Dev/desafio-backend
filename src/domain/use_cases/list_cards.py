

from src.schemas.Card import Card
from src.domain.repositories.card_repository import ICardRepository


class ListCards:

    def __init__(self, respository: ICardRepository):
        self.respository = respository

    async def perform(self, user: dict) -> list[Card]:
        cards = await self.respository.findByUserId(user.get('user_id'))
        return cards
