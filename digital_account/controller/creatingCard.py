from config import db
from digital_account.blueprints.database.read import reading_card_number_table_person_info_account
from digital_account.blueprints.database.read import reading_user_id_table_info_account
from digital_account.blueprints.return_message.jsonWithCode import sucessfully, custom_error
from digital_account.blueprints.utils.generateRandomValues import generate_char_and_number_random
from digital_account.blueprints.database.save import saving_table_card_information


def post_save_card_information(json_object: dict) -> object:
    db.create_all()

    # Checking if Card Number is on database:
    if reading_card_number_table_person_info_account(json_object["pan"]):
        data = {"error": "please, check the number of card"}
        return custom_error(data, 409)

    # Checking if user_id exists:
    if not bool(reading_user_id_table_info_account(json_object["user_id"])):
        data = {"error": f"user {json_object['user_id']} dont exists on our database"}
        return custom_error(data, 409)

    # Check if the security_code has 3 digits.
    if len(json_object["security_code"]) is not 3:
        data = {"error": "please, check the security_code information"}
        return custom_error(data, 409)

    if len(json_object["expiry_yyyy"]) is not 4 or len(json_object["expiry_mm"]) is not 2:
        data = {"error": "please, check the validity information."}
        return custom_error(data, 409)

    # Check if the valid date of card is < than actual time.
    from datetime import date
    if int(json_object["expiry_yyyy"]) <= date.today().year or int(json_object["expiry_mm"]) > 12:
        if int(json_object["expiry_yyyy"]) < date.today().year:
            data = {"error": "please, check the expiry date of your card"}
            return custom_error(data, 409)
        if int(json_object["expiry_yyyy"]) == date.today().year and int(json_object["expiry_mm"]) < date.today().month:
            data = {"error": "please, check the expiry date of your card"}
            return custom_error(data, 409)
        if int(json_object["expiry_mm"]) > 12:
            data = {"error": "please, check the expiry date of your card"}
            return custom_error(data, 409)

    # Saving information in database
    card_id = generate_char_and_number_random(size=40)
    saving_table_card_information(
        card_id=card_id,
        title=json_object["title"],
        pan=json_object["pan"],
        expiry_mm=json_object["expiry_mm"],
        expiry_yyyy=json_object["expiry_yyyy"],
        security_code=json_object["security_code"],
        date=json_object["date"],
        user_id=json_object["user_id"]
    )

    data = {
        "card_id": card_id,
        "title": json_object["title"],
        "pan": json_object["pan"],
        "expiry_mm": json_object["expiry_mm"],
        "expiry_yyyy": json_object["expiry_yyyy"],
        "security_code": json_object["security_code"],
        "date": json_object["date"],
    }
    return sucessfully(data, 201)
