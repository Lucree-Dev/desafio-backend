from fastapi import APIRouter
from src.factories.bank_statement_factory import make_bank_statement

bank = APIRouter()

@bank.get('/account/bank-statement')
async def bank_statement_controller():
    bank_statement = make_bank_statement().get('bank_statement')
    bank_statements = await bank_statement.perform()
    return bank_statements


@bank.get('/account/bank-statement/{user_id}')
async def bank_statement_controller(user_id: str):
    bank_statement = make_bank_statement().get('bank_statement')
    bank_statements = await bank_statement.perform({"user_id": user_id})
    return bank_statements