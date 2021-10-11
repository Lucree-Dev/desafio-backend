from digital_account.blueprints.database.read import reading_all_bank_statements_table
from digital_account.blueprints.return_message.jsonWithCode import sucessfully, custom_error
from config import db


def get_all_bank_statements():
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


def get_specific_bank_statement(user_id):
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
