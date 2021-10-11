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
    """
    This method is responsible for the view "/account/person" and will create a new person and save in the database.
    That method will receive all information in the body of json message with POST method.
    :return: It return a json object.
    """
    json_request = request.get_json()
    validate = validate_user_creation(json_request)

    if validate is False:
        data = {"error": "please, verify all parameters in the body of message"}
        return custom_error(data, 409)

    return post_save_user_account(json_request)


@app.route("/account/friends", methods=['GET', ])
def all_users_from_database() -> object:
    """
    This method is responsible for the view "/account/friends" and will get all informations about person in the
    database.
    This method is only allowed to receive the GET method to send the information via json.
    :return: It return a json object.
    """

    return get_all_users_table_person_info_account()


@app.route("/account/card", methods=['POST', ])
def insert_new_card() -> object:
    """
    This method is responsible for the view "/account/card" and will save the database the information about the card
    in the database.
    This method is only allowed to receive a POST method and all information must be sent in the body of json.
    :return: It return a json object.
    """

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
def all_cards_informations() -> object:
    """
    This method is responsible for the view "/account/cards" and will get all informations about the card in the
    database.
    This method is only allowed to receive a GET method and will return all information in the database.
    :return: It return a json object.
    """
    return get_all_cards_table_card_information()


@app.route("/account/transfer", methods=['POST', ])
def transfer_account() -> object:
    """
    This method is responsible for the view "/account/transfer" and will do a transfer and save it on the database.
    This method is only allowed to receive a POST method and will receive all informations about the transfer in the
    json body message.
    :return: It return a json object.
    """

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
def all_bank_statements() -> object:
    """
    This method is responsible for the view "/account/bank-statement" and will get all informations about the bank
    statement in the database.
    This method is only allowed to receive a GET method and will return all saved informations in the database via
    json
    :return: It return a json object.
    """
    return get_all_bank_statements()


@app.route("/account/bank-statement/<user_id>", methods=['GET', ])
def personal_bank_statements(user_id) -> object:
    """
    This method is responsible for the view "/account/bank-statement/<user_id>" and will get all informations about
    specific bank statement user.
    This method is only allowed to receive a GET method and will return all saved informations in the database about
    that specific user transfer.
    :return: It return a json object.
    """
    return get_specific_bank_statement(user_id)
