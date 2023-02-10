from src.schemas.Person import Person
import sqlalchemy
from src.domain.repositories.person_repository import IPersonRepository

class CreatePerson:

    def __init__(self, respository: IPersonRepository):
        self.respository = respository

    async def perform(self, person_informations: Person):
        person = self.respository.create(person_informations)
        return person
