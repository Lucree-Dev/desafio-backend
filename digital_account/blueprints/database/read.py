from digital_account.models.PersonModel import db as db_user_information
from digital_account.models.PersonModel import PersonInfoAccount
from digital_account.models.Cards import db as db_card_information
from digital_account.models.Cards import PersonCardInformation
from digital_account.models.BankStatement import db as db_bank_statement
from digital_account.models.BankStatement import BankInformations


def reading_username_table_person_info_account(username: str) -> object:
    """
    Reading the information in database at the table (person-info-account). That method will read a specific user
    and return the information about that username. If the username dont exists in database, it will return None.


    :param username: A username specific do search in database.
    :return: It will return a object with the informations about the username or will return a null object.
    """
    return PersonInfoAccount.query.filter_by(username=username).first()


def reading_card_number_table_person_info_account(card: str) -> object:
    """
    That method read the database in the table (card-information). That method receive a card number and will
    search in dabase.

    :param card: A card number with try search in database in the table card-information)
    :return: It will return the object with the informations about the card or will return a null object.
    """
    return PersonCardInformation.query.filter_by(pan=card).first()


def reading_all_users_table_person_info_account() -> list:
    """
    That method will read all users from database in the table person-info-account.
    :return: It will return a list of user to manipulate.
    """
    users = []

    users_informations = db_user_information.session.query(PersonInfoAccount).all()

    for user in users_informations:
        users.append(user)

    return users


def reading_all_cards_table_card_information() -> list:
    """
        That method will read all users from database in the table card-information.
        :return: It will return a list of user to manipulate.
        """
    cards = []

    cards_information = db_card_information.session.query(PersonCardInformation).all()

    for card in cards_information:
        cards.append(card)

    return cards


def reading_user_id_table_info_account(user_id: str) -> object:
    """
    That method will read the information about user_id in the database. If the user_id is unavailable
    it will return a null object.

    :param user_id: The information about the user_id to search in database.
    :return: It will return a object with informations about user_id or will return none object.
    """
    return PersonInfoAccount.query.filter_by(user_id=user_id).first()


def reading_card_id_table_person_card_information(card_id: str) -> object:
    """
    That method will read a information about card_id in the database at the table card-information. That
    method will return a object with information if find any information or will return the none object.

    :param card_id: A string with card_id information to find in the database.
    :return: It will return a object with the informations about card_id find in the database or will return a null
            object.
    """
    return PersonCardInformation.query.filter_by(card_id=card_id).first()


def reading_all_bank_statements_table() -> list:
    """
    That method will read all informations in the database at the table bank-informations. That method will create
    a list to add that information and will return it.

    :return: A list with all bank statements find in the database.
    """
    bank_statements = []

    bank_statement = db_bank_statement.session.query(BankInformations).all()

    for statement in bank_statement:
        bank_statements.append(statement)

    return bank_statements
