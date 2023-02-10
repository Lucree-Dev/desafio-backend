from src.domain.repositories.person_repository import IPersonRepository

class ListFriends:

    def __init__(self, respository: IPersonRepository):
        self.respository = respository

    async def perform(self):
        friends = self.respository.findAll()
        return friends