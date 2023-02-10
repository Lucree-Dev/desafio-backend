import abc

from src.schemas.Card import Card


class ICardRepository(abc.ABC):
    @abc.abstractmethod
    async def create() -> str:
        """Creates a card"""

    @abc.abstractmethod
    async def findByUserId(user_id: str) -> str:
        """List all cards"""
