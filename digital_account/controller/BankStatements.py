from digital_account.blueprints.database.read import reading_all_bank_statements_table
from digital_account.blueprints.return_message.jsonWithCode import sucessfully, custom_error
from config import db


def get_all_bank_statements() -> object:
    """
    That method will get all information in the database at the table "bank-statement". It will add a information
    in one list and will generate a json to return in the view.
    :return: It return a object with json information and the status code of page.
    """

    db.create_all()
    bank_statements = reading_all_bank_statements_table()
    single_bank_statement = []

    for bank_statement in bank_statements:
        year = str(bank_statement.date_created)[:4]
        month = str(bank_statement.date_created)[5:7]
        day = str(bank_statement.date_created)[8:10]

        statement = {
            "user_id": bank_statement.user_id,
            "friend_id": bank_statement.friend_id,
            "value": bank_statement.value,
            "date": f"{day}/{month}/{year}",
            "from_card": bank_statement.from_card,
        }

        single_bank_statement.append(statement)

    return sucessfully(single_bank_statement, 200)


def get_specific_bank_statement(user_id: str) -> object:
    """
    That method will get all information in the database at the table "bank-statement" and will return information
    about specific user_id (received in the parameter) If a user_id is not find in the table it will return None with
    status code 404.

    :param user_id: A user_id information to verify if has some information in database to return in the endpoint.
    :return: It will return a information of transaction with status code 200 or if dont find any transaction it
             will return a 404 status code with a specific error.
    """
    db.create_all()
    bank_statements = reading_all_bank_statements_table()
    single_bank_statement = []

    for bank_statement in bank_statements:
        if user_id == bank_statement.user_id:
            year = str(bank_statement.date_created)[:4]
            month = str(bank_statement.date_created)[5:7]
            day = str(bank_statement.date_created)[8:10]

            statement = {
                "user_id": bank_statement.user_id,
                "friend_id": bank_statement.friend_id,
                "value": bank_statement.value,
                "date": f"{day}/{month}/{year}",
                "from_card": bank_statement.from_card,
            }

            single_bank_statement.append(statement)

    if not single_bank_statement:
        data = {"error": "no transition for that user_id"}
        return custom_error(data, 404)

    return sucessfully(single_bank_statement, 200)
