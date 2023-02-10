from src.schemas.Person import Person


class PersonMapper:

    @staticmethod
    def toController(person: Person):
        password_length = len(person.password)
        anonymize = "*" * password_length
        return {
            "first_name": person.first_name,
            "last_name": person.last_name,
            "birthday": person.birthday,
            "password": anonymize,
            "user_id": person.user_id,
            "username": person.username
        }
