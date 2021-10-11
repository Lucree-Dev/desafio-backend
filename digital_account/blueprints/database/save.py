from digital_account.models.PersonModel import db as db_person
from digital_account.models.PersonModel import PersonInfoAccount
from digital_account.models.Cards import db as db_card
from digital_account.models.Cards import PersonCardInformation
from digital_account.models.BankStatement import db as db_bank_statement
from digital_account.models.BankStatement import BankInformations


def saving_table_person_info_account(
        first_name: str, last_name: str, birthday: str, password: str, username: str, user_id: str
) -> None:
    """
    That method will save the information in the database at the table "person-info-account". That method receive some
    param to save in the database. That informations received must be treated before come to that method.

    :param first_name: The first name of user to save in the database.
    :param last_name: The last name of user to save in the database.
    :param birthday: The birthday of user to save in the database.
    :param password: The password of user to save in the database.
    :param username: The username (it must be unique) of user to save in the database.
    :param user_id: The user_id of user to save in the database.
    :return: It return None.
    """

    db_person.session.add(PersonInfoAccount(
        first_name=first_name,
        last_name=last_name,
        birthday=birthday,
        password=password,
        username=username,
        user_id=user_id
    ))
    db_person.session.commit()


def saving_table_card_information(
        card_id: str, title: str, pan: str, expiry_mm: str, expiry_yyyy: str, security_code: str, date: str, user_id: str
) -> None:
    """
    That method will save the information in the database at the table "card-information". That method receive some
    param to save in the database. That informations received must be treated before come to that method.

    :param card_id: It receive the card_id information to save in the database.
    :param title: It receive the card Title to save in the database.
    :param pan: It receive the pan (card number) to save in the database.
    :param expiry_mm: It receive the expire month (with 2 digits) to save in the database.
    :param expiry_yyyy:  It receive the year (with 4 digits) to save in the database.
    :param security_code: It receive the security code (with 3 digits) to save in the database.
    :param date: It receive the date of expiration card to save in the database.
    :param user_id: It receive the user_id to vinculate with that user.
    :return: It return None.
    """

    db_card.session.add(PersonCardInformation(
        card_id=card_id,
        title=title,
        pan=pan,
        expiry_mm=expiry_mm,
        expiry_yyyy=expiry_yyyy,
        security_code=security_code,
        date=date,
        user_id=user_id,
    ))
    db_card.session.commit()


def saving_transfer_value(user_id: str, friend_id: str, value: int, from_card: str) -> None:
    """
    That method will save the information in the database at the table "bank-informations". That method receive some
    param to save in the database. That informations received must be treated before come to that method.

    :param user_id: It will receive the user_id to save in the database.
    :param friend_id: It will receive the friend_id (information about how will receive the payment) to save in the
           database
    :param value: It will receive the value of transition to save in the database.
    :param from_card: It will receive the information about card to save in the database.
    :return: It return None.
    """

    db_bank_statement.session.add(BankInformations(
        user_id=user_id,
        friend_id=friend_id,
        value=value,
        from_card=from_card,
    ))
    db_card.session.commit()
