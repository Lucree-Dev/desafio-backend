from unittest import TestCase
import requests
import json

from config import HOST, PORT
from digital_account.blueprints.utils.generateRandomValues import randomic_letters_uppercase
from digital_account.blueprints.utils.generateRandomValues import generate_char_and_number_random
from digital_account.blueprints.utils.generateRandomValues import generate_random_number

URL_ADRESS = f"http://{HOST}:{PORT}/account/transfer"


class ViewAccountTransferAPI(TestCase):
    header = {'content-type': 'application/json'}

    def test_status_code_page_with_get(self):
        # Title: Access the page and check the status Code
        # step 1: Access the page and verify the status_code of the page
        # Expected Result: It should return the status_code = 405 (method not allowed)
        req_get = requests.get(url=URL_ADRESS)
        self.assertEqual(req_get.status_code, 405)

    def test_do_a_transfer_sucessfully(self):
        # Title: Do a valid transfer and check its sucessfully.
        # step 1: Access the endpoint to create a new user and create 2 valids user
        # step 2: Access the endpoint to vinculate the CARD and vinculate 2 new cards ( 1 to each ).
        # step 3: Do de transfer and verify the status_code of the page.

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
        req_card = requests.post(url=f"http://{HOST}:{PORT}/account/card", data=json.dumps(data_card), headers=self.header)
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
        req_card = requests.post(url=f"http://{HOST}:{PORT}/account/card", data=json.dumps(data_card), headers=self.header)
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
            "total_to_transfer": 100,
            "billing_card": {
                "card_id": first_card_id
            }
        }

        req_transfer = requests.post(url=URL_ADRESS, data=json.dumps(data), headers=self.header)
        self.assertEqual(req_transfer.status_code, 201)

    def test_do_a_transfer_without_friend_id(self):
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
            "total_to_transfer": 100,
            "billing_card": {
                "card_id": first_card_id
            }
        }

        req_transfer = requests.post(url=URL_ADRESS, data=json.dumps(data), headers=self.header)
        self.assertEqual(req_transfer.status_code, 409)

    def test_do_a_transfer_without_total_to_transfer(self):
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
            "billing_card": {
                "card_id": first_card_id
            }
        }

        req_transfer = requests.post(url=URL_ADRESS, data=json.dumps(data), headers=self.header)
        self.assertEqual(req_transfer.status_code, 409)

    def test_do_a_transfer_without_billing_card(self):
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
            "total_to_transfer": 100,
        }

        req_transfer = requests.post(url=URL_ADRESS, data=json.dumps(data), headers=self.header)
        self.assertEqual(req_transfer.status_code, 409)

    def test_do_a_transfer_without_card_id(self):
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
            "total_to_transfer": 100,
            "billing_card": {
                "": "",
            }
        }

        req_transfer = requests.post(url=URL_ADRESS, data=json.dumps(data), headers=self.header)
        self.assertEqual(req_transfer.status_code, 409)

    def test_do_a_transfer_with_invalid_card_id(self):
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
            "total_to_transfer": 100,
            "billing_card": {
                "card_id": generate_char_and_number_random(size=30),
            }
        }

        req_transfer = requests.post(url=URL_ADRESS, data=json.dumps(data), headers=self.header)
        self.assertEqual(req_transfer.status_code, 404)

    def test_do_a_transfer_to_yourself(self):
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
            "friend_id": first_user_id_information,
            "total_to_transfer": 100,
            "billing_card": {
                "card_id": first_card_id
            }
        }

        req_transfer = requests.post(url=URL_ADRESS, data=json.dumps(data), headers=self.header)
        self.assertEqual(req_transfer.status_code, 409)

    def test_do_a_transfer_to_invalid_friend_id(self):
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
            "friend_id": randomic_letters_uppercase(length=30),
            "total_to_transfer": 100,
            "billing_card": {
                "card_id": first_card_id
            }
        }

        req_transfer = requests.post(url=URL_ADRESS, data=json.dumps(data), headers=self.header)
        self.assertEqual(req_transfer.status_code, 404)

    def test_do_a_transfer_with_invalid_user_id(self):
        ...
