from src.factories.list_friends_factory import make_list_friends
from fastapi import APIRouter
from src.factories.create_person_factory import make_create_person
from src.schemas.Person import Person

person = APIRouter()

@person.post('/account/person', status_code=201)
async def create_person_controller(person_informations: Person):
    create_person = make_create_person().get('create_person')

    person = await create_person.perform({
        "first_name": person_informations.first_name,
        "last_name": person_informations.last_name,
        "birthday": person_informations.birthday,
        "password": person_informations.password,
        "username": person_informations.username
    })

    return person

@person.get('/account/friends')
async def list_friends_controller():
    list_friends = make_list_friends().get('list_friends')
    friends = await list_friends.perform()

    return friends