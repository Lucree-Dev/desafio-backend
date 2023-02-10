import abc

from src.schemas.Person import Person


class IPersonRepository(abc.ABC):
    @abc.abstractmethod
    async def create() -> str:
        """Creates a person"""

    @abc.abstractmethod
    async def findAll() -> list[Person]:
        """List all friends"""
