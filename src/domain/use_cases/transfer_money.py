from src.schemas.Card import Card
from src.domain.repositories.transfer_repository import ITransferRepository


class TransferMoney:

    def __init__(self, respository: ITransferRepository):
        self.respository = respository

    async def perform(self, transfer_informations: Card):
        transfer_id = await self.respository.create(transfer_informations)
        return transfer_id
