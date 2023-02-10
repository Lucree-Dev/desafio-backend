from src.infra.sqlalchemy.person_repository import PersonRepository
from src.domain.use_cases.create_person import CreatePerson


def make_create_person():
    person_repository = PersonRepository()
    create_person = CreatePerson(person_repository)

    return {
        "create_person": create_person
    }