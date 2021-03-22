from fastapi import FastAPI

from auth.router import token
from routers.cards import card as card_router
from routers.friends import friends as friends_router
from routers.person import person as person_router
from routers.transfer import transfer as transfer_router
from routers.bank import bank as bank_router

app = FastAPI()
app.include_router(token)
app.include_router(person_router, prefix="/account")
app.include_router(friends_router, prefix="/account")
app.include_router(card_router, prefix="/account")
app.include_router(transfer_router, prefix="/account")
app.include_router(bank_router, prefix="/account")
