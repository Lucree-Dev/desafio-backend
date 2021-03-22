from fastapi import APIRouter
from fastapi import Depends

from auth.auth import auth_wrapper
from db import Friends as FriendsORM
from db import Person as PersonORM
from db import SQLITE_DB

friends = APIRouter()


@friends.get("/friends")
def get_friends_by_person(username=Depends(auth_wrapper)):
    try:
        with SQLITE_DB.atomic():
            person = PersonORM.select().where(PersonORM.username == username).get()
            friends_list = []

            query = (PersonORM
                     .select()
                     .join(FriendsORM, on=FriendsORM.to_user)
                     .where(FriendsORM.from_user == person))

            for friend in query:
                friend_dict = {
                    "first_name": friend.first_name,
                    "last_name": friend.last_name,
                    "birthday": friend.birthday,
                    "username": friend.username,
                    "user_id": friend.user_id
                }

                friends_list.append(friend_dict)

            return friends_list

    except Exception as error:
        raise error
