from digital_account.models.PersonModel import db as db_user_information
from digital_account.models.PersonModel import PersonInfoAccount
from digital_account.models.Cards import db as db_card_information
from digital_account.models.Cards import PersonCardInformation
from digital_account.models.BankStatement import db as db_bank_statement
from digital_account.models.BankStatement import BankInformations


def reading_username_table_person_info_account(username: str) -> object:
    return PersonInfoAccount.query.filter_by(username=username).first()


def reading_card_number_table_person_info_account(card: str) -> object:
    return PersonCardInformation.query.filter_by(pan=card).first()


def reading_all_users_table_person_info_account():
    users = []

    users_informations = db_user_information.session.query(PersonInfoAccount).all()

    for user in users_informations:
        users.append(user)

    return users


def reading_all_cards_table_card_information():
    cards = []

    cards_information = db_card_information.session.query(PersonCardInformation).all()

    for card in cards_information:
        cards.append(card)

    return cards


def reading_user_id_table_info_account(user_id):
    return PersonInfoAccount.query.filter_by(user_id=user_id).first()


def reading_card_id_table_person_card_information(card_id):
    return PersonCardInformation.query.filter_by(card_id=card_id).first()


def reading_all_bank_statements_table():
    bank_statements = []

    bank_statement = db_bank_statement.session.query(BankInformations).all()

    for statement in bank_statement:
        bank_statements.append(statement)

    return bank_statements
