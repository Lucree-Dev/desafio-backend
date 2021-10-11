from digital_account.blueprints.database.read import reading_all_users_table_person_info_account
from digital_account.blueprints.return_message.jsonWithCode import sucessfully
from config import db


def get_all_users_table_person_info_account() -> object:
    """
    That method will get all informations in the database at the table person-info-account and will do a list to return.
    :return: It will return a json object with page status page.
    """

    db.create_all()
    users = []

    for user in reading_all_users_table_person_info_account():
        single_user = {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "birthday": user.birthday,
            "username": user.username,
            "user_id": user.user_id,
        }

        users.append(single_user)

    return sucessfully(users, 200)
