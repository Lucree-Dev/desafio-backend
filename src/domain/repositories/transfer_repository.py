import abc

class ITransferRepository(abc.ABC):
    @abc.abstractmethod
    async def create() -> str:
        """Creates a card"""