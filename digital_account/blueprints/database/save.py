from digital_account.models.PersonModel import db as db_person
from digital_account.models.PersonModel import PersonInfoAccount
from digital_account.models.Cards import db as db_card
from digital_account.models.Cards import PersonCardInformation
from digital_account.models.BankStatement import db as db_bank_statement
from digital_account.models.BankStatement import BankInformations


def saving_table_person_info_account(
        first_name: str, last_name: str, birthday: str, password: str, username: str, user_id: str
):
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
):
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


def saving_transfer_value(user_id: str, friend_id: str, value: int, from_card: str):
    db_bank_statement.session.add(BankInformations(
        user_id=user_id,
        friend_id=friend_id,
        value=value,
        from_card=from_card,
    ))
    db_card.session.commit()
