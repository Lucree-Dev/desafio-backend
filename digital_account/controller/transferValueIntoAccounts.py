from digital_account.blueprints.return_message.jsonWithCode import custom_error, sucessfully
from digital_account.blueprints.database.read import reading_user_id_table_info_account
from digital_account.blueprints.database.read import reading_all_cards_table_card_information
from digital_account.blueprints.database.save import saving_transfer_value
from config import db


def transfer_values(json_request):
    db.create_all()
    user_db = reading_user_id_table_info_account(user_id=json_request["user_id"])
    friend_db = reading_user_id_table_info_account(json_request["friend_id"])
    cards_from_user_db = []

    # Check if user_id = friend_id:
    if json_request["user_id"] == json_request["friend_id"]:
        data = {"error": "The user_id and friend_id look likes the same."}
        return custom_error(data, 409)

    # Check if the user_id and friend_id in on database
    if user_db is None or friend_db is None:
        if user_db is None:
            data = {"error": "user_id not found"}
            return custom_error(data, 404)
        data = {"error": "friend_id not found"}
        return custom_error(data, 404)

    # Get all cards from user (if available).
    for card in reading_all_cards_table_card_information():
        if user_db.user_id == card.user_id:
            cards_from_user_db.append(card.card_id)

    # Check if card in the body contains in the cards_from_user_db
    if json_request["billing_card"]["card_id"] not in cards_from_user_db:
        data = {"error": "please, check the card number"}
        return custom_error(data, 404)

    # saving in database the transaction.
    saving_transfer_value(
        user_id=json_request["user_id"],
        friend_id=json_request["user_id"],
        value=json_request["total_to_transfer"],
        from_card=json_request["billing_card"]["card_id"]
    )

    data = {
        "user_id": json_request["user_id"],
        "friend_id": json_request["friend_id"],
        "total_to_transfer": json_request["total_to_transfer"],
        "from_card": json_request["billing_card"]["card_id"],
    }

    return sucessfully(data, 201)