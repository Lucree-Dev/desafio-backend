from digital_account.blueprints.database.read import reading_all_cards_table_card_information
from digital_account.blueprints.return_message.jsonWithCode import sucessfully
from config import db


def get_all_cards_table_card_information() -> object:
    """
    That method will get all informations in the database, in the table "card-informations" and will genrate a list
    to return it.
    :return: It will return a json object with the page status code.
    """

    db.create_all()
    cards = []

    for card in reading_all_cards_table_card_information():
        single_card = {
            "title": card.title,
            "pan": card.pan,
            "expiry_mm": card.expiry_mm,
            "expiry_yyyy": card.expiry_yyyy,
            "security_code": card.security_code,
            "date": card.date
        }

        cards.append(single_card)

    return sucessfully(cards, 200)
