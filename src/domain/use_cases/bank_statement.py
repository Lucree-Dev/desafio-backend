from src.schemas.Card import Card
from src.domain.repositories.card_repository import ICardRepository


class BankStatement:

    def __init__(self, respository: ICardRepository):
        self.respository = respository

    async def perform(self, user_id: str):
        statement_id = await self.respository.findByUserId(user_id)
        return {"statement_id": statement_id.get('statement_id')}
