from unittest import TestCase
import requests
import json

from config import HOST, PORT
from digital_account.blueprints.utils.generateRandomValues import randomic_letters_uppercase
from digital_account.blueprints.utils.generateRandomValues import generate_char_and_number_random
from digital_account.blueprints.utils.generateRandomValues import generate_random_number

URL_ADRESS = f"http://{HOST}:{PORT}/account/bank-statement"


class ViewAccountFriendsAPI(TestCase):
    header = {'content-type': 'application/json'}

    def test_status_code_with_get_method(self):
        req_get = requests.get(url=URL_ADRESS)
        self.assertEqual(req_get.status_code, 200)

    def test_create_transfer_account_and_check_it_on_all_statements(self):
        # Create first user
        first_user = randomic_letters_uppercase(length=10)
        first_card_number_information = generate_random_number(16)
        first_user_id_information = str
        first_card_id = str

        data = {
            "first_name": first_user,
            "last_name": randomic_letters_uppercase(length=20),
            "birthday": "01/01/1999",
            "password": generate_char_and_number_random(size=30),
            "username": generate_char_and_number_random(size=30),
        }
        requests.post(url=f"http://{HOST}:{PORT}/account/person", data=json.dumps(data), headers=self.header)

        req_get = requests.get(url=f"http://{HOST}:{PORT}/account/friends")
        for user in req_get.json():
            if user["first_name"] == first_user:
                first_user_id_information = user["user_id"]

        data_card = {
            "title": randomic_letters_uppercase(length=10),
            "user_id": first_user_id_information,
            "pan": first_card_number_information,
            "expiry_mm": "01",
            "expiry_yyyy": "2999",
            "security_code": "123",
            "date": "12/12/2999",
        }
        req_card = requests.post(url=f"http://{HOST}:{PORT}/account/card", data=json.dumps(data_card),
                                 headers=self.header)
        self.assertEqual(req_card.status_code, 201)

        # Create secound user
        secound_user = randomic_letters_uppercase(length=10)
        second_card_number_information = generate_random_number(16)
        second_user_id_information = str

        data = {
            "first_name": secound_user,
            "last_name": randomic_letters_uppercase(length=20),
            "birthday": "01/01/1999",
            "password": generate_char_and_number_random(size=30),
            "username": generate_char_and_number_random(size=30),
        }
        requests.post(url=f"http://{HOST}:{PORT}/account/person", data=json.dumps(data), headers=self.header)

        req_get = requests.get(url=f"http://{HOST}:{PORT}/account/friends")
        for user in req_get.json():
            if user["first_name"] == secound_user:
                second_user_id_information = user["user_id"]

        data_card = {
            "title": randomic_letters_uppercase(length=10),
            "user_id": second_user_id_information,
            "pan": second_card_number_information,
            "expiry_mm": "01",
            "expiry_yyyy": "2999",
            "security_code": "123",
            "date": "12/12/2999",
        }
        req_card = requests.post(url=f"http://{HOST}:{PORT}/account/card", data=json.dumps(data_card),
                                 headers=self.header)
        self.assertEqual(req_card.status_code, 201)

        # Getting the card_id from first users
        from digital_account.blueprints.database.read import reading_all_cards_table_card_information
        for card in reading_all_cards_table_card_information():
            if card.user_id == first_user_id_information:
                first_card_id = card.card_id

        # Doing a transfer
        data = {
            "user_id": first_user_id_information,
            "friend_id": second_user_id_information,
            "total_to_transfer": generate_random_number(length=4),
            "billing_card": {
                "card_id": first_card_id
            }
        }

        req_transfer = requests.post(url=f"http://{HOST}:{PORT}/account/transfer", data=json.dumps(data), headers=self.header)
        self.assertEqual(req_transfer.status_code, 201)

        # check the user_id and friend_id and check the card information.
        transfer_statement = False
        req_get = requests.get(url=URL_ADRESS)
        for statement in req_get.json():
            if statement["user_id"] == first_user_id_information:
                transfer_statement = True

        assert transfer_statement

    def test_create_transfer_and_check_it_on_user_statement(self):
        first_user = randomic_letters_uppercase(length=10)
        first_card_number_information = generate_random_number(16)
        first_user_id_information = str
        first_card_id = str

        data = {
            "first_name": first_user,
            "last_name": randomic_letters_uppercase(length=20),
            "birthday": "01/01/1999",
            "password": generate_char_and_number_random(size=30),
            "username": generate_char_and_number_random(size=30),
        }
        requests.post(url=f"http://{HOST}:{PORT}/account/person", data=json.dumps(data), headers=self.header)

        req_get = requests.get(url=f"http://{HOST}:{PORT}/account/friends")
        for user in req_get.json():
            if user["first_name"] == first_user:
                first_user_id_information = user["user_id"]

        data_card = {
            "title": randomic_letters_uppercase(length=10),
            "user_id": first_user_id_information,
            "pan": first_card_number_information,
            "expiry_mm": "01",
            "expiry_yyyy": "2999",
            "security_code": "123",
            "date": "12/12/2999",
        }
        req_card = requests.post(url=f"http://{HOST}:{PORT}/account/card", data=json.dumps(data_card),
                                 headers=self.header)
        self.assertEqual(req_card.status_code, 201)

        # Create secound user
        secound_user = randomic_letters_uppercase(length=10)
        second_card_number_information = generate_random_number(16)
        second_user_id_information = str

        data = {
            "first_name": secound_user,
            "last_name": randomic_letters_uppercase(length=20),
            "birthday": "01/01/1999",
            "password": generate_char_and_number_random(size=30),
            "username": generate_char_and_number_random(size=30),
        }
        requests.post(url=f"http://{HOST}:{PORT}/account/person", data=json.dumps(data), headers=self.header)

        req_get = requests.get(url=f"http://{HOST}:{PORT}/account/friends")
        for user in req_get.json():
            if user["first_name"] == secound_user:
                second_user_id_information = user["user_id"]

        data_card = {
            "title": randomic_letters_uppercase(length=10),
            "user_id": second_user_id_information,
            "pan": second_card_number_information,
            "expiry_mm": "01",
            "expiry_yyyy": "2999",
            "security_code": "123",
            "date": "12/12/2999",
        }
        req_card = requests.post(url=f"http://{HOST}:{PORT}/account/card", data=json.dumps(data_card),
                                 headers=self.header)
        self.assertEqual(req_card.status_code, 201)

        # Getting the card_id from first users
        from digital_account.blueprints.database.read import reading_all_cards_table_card_information
        for card in reading_all_cards_table_card_information():
            if card.user_id == first_user_id_information:
                first_card_id = card.card_id

        # Doing a transfer
        data = {
            "user_id": first_user_id_information,
            "friend_id": second_user_id_information,
            "total_to_transfer": generate_random_number(length=4),
            "billing_card": {
                "card_id": first_card_id
            }
        }

        req_transfer = requests.post(url=f"http://{HOST}:{PORT}/account/transfer", data=json.dumps(data),
                                     headers=self.header)
        self.assertEqual(req_transfer.status_code, 201)

        # check the user_id page bank statement.
        req_get = requests.get(url=URL_ADRESS + f'/{first_user_id_information}')
        self.assertEqual(req_get.status_code, 200)

    def test_check_invalid_statement_and_verify_the_404(self):
        first_user = randomic_letters_uppercase(length=30)
        req_get = requests.get(url=URL_ADRESS + f'/{first_user}')
        self.assertEqual(req_get.status_code, 404)
