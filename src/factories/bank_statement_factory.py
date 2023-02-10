from src.domain.use_cases.bank_statement import BankStatement
from src.infra.sqlalchemy.statement_repository import StatementRepository


def make_bank_statement():
    statement_repository = StatementRepository()
    bank_statement = BankStatement(statement_repository)

    return {
        "bank_statement": bank_statement
    }