from src.domain.repositories.statement_repository import IStatementRepository

class StatementRepository(IStatementRepository):

    @staticmethod
    async def findByUserId(informations):
        print(informations)
        return {
            "statement_id": "statement_id",
        }