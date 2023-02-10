from src.domain.use_cases.transfer_money import TransferMoney
from src.infra.sqlalchemy.transfer_repository import TransferRepository


def make_transfer_money():
    card_repository = TransferRepository()
    transfer_money = TransferMoney(card_repository)

    return {
        "transfer_money": transfer_money
    }