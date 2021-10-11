from digital_account.blueprints.return_message.jsonWithCode import sucessfully, custom_error
from digital_account.blueprints.database.save import saving_table_person_info_account
from digital_account.blueprints.database.read import reading_username_table_person_info_account
from digital_account.blueprints.utils.generateRandomValues import generate_char_and_number_random
from config import db

from werkzeug.security import generate_password_hash


def post_save_user_account(json_object: dict) -> object:
    db.create_all()

    # Checking if username is on database, if yes, it return the error to create another username.
    if reading_username_table_person_info_account(json_object["username"]):
        data = {"error": "that username is already created"}
        return custom_error(data, 409)

    # saving informations in database
    user_id = generate_char_and_number_random(size=40)
    password_hashed = generate_password_hash(json_object["password"], "sha256")

    saving_table_person_info_account(
        first_name=json_object["first_name"],
        last_name=json_object["last_name"],
        birthday=json_object["birthday"],
        password=password_hashed,
        username=json_object["username"],
        user_id=user_id
    )

    # creating json to return in sucessfully message
    data = {
        "first_name": json_object["first_name"],
        "last_name": json_object["last_name"],
        "birthday": json_object["birthday"],
        "password": password_hashed,
        "username": json_object["username"],
        "user_id": user_id
    }
    return sucessfully(data, 201)



