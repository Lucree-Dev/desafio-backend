from fastapi import FastAPI
from src.routes.person_routes import person
from src.routes.cards_routes import cards
from src.routes.transfer_routes import transfer
from src.routes.bank_routes import bank

server = FastAPI()

server.include_router(person)
server.include_router(cards)
server.include_router(transfer)
server.include_router(bank)

