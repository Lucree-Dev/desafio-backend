from flask import request

from config import app
from digital_account.blueprints.return_message.jsonWithCode import custom_error

from digital_account.blueprints.validators.Validations import validate_user_creation
from digital_account.blueprints.validators.Validations import validate_card
from digital_account.blueprints.validators.Validations import validate_account_transfer
from digital_account.controller.BankStatements import get_all_bank_statements
from digital_account.controller.BankStatements import get_specific_bank_statement
from digital_account.controller.creatingUserAccount import post_save_user_account
from digital_account.controller.showAllUsers import get_all_users_table_person_info_account
from digital_account.controller.showAllCards import get_all_cards_table_card_information
from digital_account.controller.transferValueIntoAccounts import transfer_values
from digital_account.controller.creatingCard import post_save_card_information


@app.route("/account/person", methods=['POST', ])
def create_user_account() -> object:
    json_request = request.get_json()
    validate = validate_user_creation(json_request)

    if validate is False:
        data = {"error": "please, verify all parameters in the body of message"}
        return custom_error(data, 409)

    return post_save_user_account(json_request)


@app.route("/account/friends", methods=['GET', ])
def all_users_from_database():
    return get_all_users_table_person_info_account()


@app.route("/account/card", methods=['POST', ])
def insert_new_card():
    if request.get_json() is None:
        data = {"error": "please, send the information in the body of message"}
        return custom_error(data, 409)

    json_request = request.get_json()
    validate = validate_card(json_request)

    if validate is False:
        data = {"error": "please, verify all parameters in the body of message"}
        return custom_error(data, 409)

    return post_save_card_information(json_request)


@app.route("/account/cards", methods=['GET', ])
def all_cards_informations():
    return get_all_cards_table_card_information()


@app.route("/account/transfer", methods=['POST', ])
def transfer_account():
    if request.get_json() is None:
        data = {"error": "please, send the information in the body of message"}
        return custom_error(data, 409)

    json_request = request.get_json()
    validate = validate_account_transfer(json_request)

    # check if all paramentrs in the body of message
    if validate is False:
        data = {"error": "please, verify all parameters in the body of message"}
        return custom_error(data, 409)

    return transfer_values(json_request)


@app.route("/account/bank-statement", methods=['GET', ])
def all_bank_statements():
    return get_all_bank_statements()


@app.route("/account/bank-statement/<user_id>", methods=['GET',])
def personal_bank_statements(user_id):
    return get_specific_bank_statement(user_id)
