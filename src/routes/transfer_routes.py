from fastapi import APIRouter
from src.factories.transfer_money_factory import make_transfer_money
from src.schemas.Transfer import Transfer

transfer = APIRouter()

@transfer.post('/account/transfer')
async def transfers_controller(transfer_information: Transfer):
    transfer_money = make_transfer_money().get('transfer_money')
    transfer = await transfer_money.perform({
        "friend_id": transfer_information.friend_id,
        "total_to_transfer": transfer_information.total_to_transfer,
        "billing_card": {
            "card_id": transfer_information.billing_card.card_id
        }
    })

    return transfer
