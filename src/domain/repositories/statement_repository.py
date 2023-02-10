import abc

class IStatementRepository(abc.ABC):

    @abc.abstractmethod
    async def findByUserId(user_id: str) -> str:
        """List all cards"""