from src.domain.use_cases.list_friends import ListFriends
from src.infra.sqlalchemy.person_repository import PersonRepository

def make_list_friends():
    person_repository = PersonRepository()
    list_friends = ListFriends(person_repository)

    return {
        "list_friends": list_friends
    }