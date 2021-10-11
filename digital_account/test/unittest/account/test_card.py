from unittest import TestCase
import requests
import json

from config import HOST, PORT
from digital_account.blueprints.utils.generateRandomValues import randomic_letters_uppercase
from digital_account.blueprints.utils.generateRandomValues import generate_char_and_number_random
from digital_account.blueprints.utils.generateRandomValues import generate_random_number

URL_ADRESS = f"http://{HOST}:{PORT}/account/card"


class ViewAccountCardAPI(TestCase):
    header = {'content-type': 'application/json'}

    def test_status_code_page_with_get(self):
        # Title: Access the page and check the status Code
        # step 1: Access the page and verify the status_code of the page
        # Expected Result: It should return the status_code = 405 (method not allowed)
        req_get = requests.get(url=URL_ADRESS)
        self.assertEqual(req_get.status_code, 405)

    def test_create_new_card_and_vinculate_with_valid_user(self):
        # Title: Create a new Card with valid User and check it return the correct status_code
        # step 1: Create a new user (from Person API) and get the user_id from response
        # step 2: Create a new card with user created in step 1
        # step 3: Verify the API will return the status_code = 201
        # Expected Result: The API must return the 201 status_code and create the Card
        first_name = randomic_letters_uppercase(length=10)
        data = {
            "first_name": first_name,
            "last_name": randomic_letters_uppercase(length=20),
            "birthday": "01/01/1999",
            "password": generate_char_and_number_random(size=30),
            "username": generate_char_and_number_random(size=30),
        }
        requests.post(url=f"http://{HOST}:{PORT}/account/person", data=json.dumps(data), headers=self.header)

        req_get = requests.get(url=f"http://{HOST}:{PORT}/account/friends")
        user_id_information = ""
        for user in req_get.json():
            if user["first_name"] == first_name:
                user_id_information = user["user_id"]

        data_card = {
            "title": randomic_letters_uppercase(length=10),
            "user_id": user_id_information,
            "pan": generate_random_number(16),
            "expiry_mm": "01",
            "expiry_yyyy": "2999",
            "security_code": "123",
            "date": "12/12/2999",
        }
        req_card = requests.post(url=f"{URL_ADRESS}", data=json.dumps(data_card), headers=self.header)
        self.assertEqual(req_card.status_code, 201)

    def test_create_new_card_and_vinculate_with_invalid_user(self):
        # Title: Create a new Card with invalid User and check it return the correct status_code
        # step 1: Create a new card with invalid user
        # step 3: Verify the API will return the status_code = 409
        # Expected Result: The API must return the 409 status_code and create the Card
        data = {
            "title": randomic_letters_uppercase(length=10),
            "user_id": generate_char_and_number_random(size=30),
            "pan": generate_random_number(16),
            "expiry_mm": "01",
            "expiry_yyyy": "2999",
            "security_code": "123",
            "date": "12/12/2999",
        }
        req_card = requests.post(url=f"{URL_ADRESS}", data=json.dumps(data), headers=self.header)
        self.assertEqual(req_card.status_code, 409)

    def test_create_new_card_and_repete_pan_in_another_execution(self):
        first_name = randomic_letters_uppercase(length=10)
        pan_card = generate_random_number(16)

        data = {
            "first_name": first_name,
            "last_name": randomic_letters_uppercase(length=20),
            "birthday": "01/01/1999",
            "password": generate_char_and_number_random(size=30),
            "username": generate_char_and_number_random(size=30),
        }
        requests.post(url=f"http://{HOST}:{PORT}/account/person", data=json.dumps(data), headers=self.header)

        req_get = requests.get(url=f"http://{HOST}:{PORT}/account/friends")
        user_id_information = ""
        for user in req_get.json():
            if user["first_name"] == first_name:
                user_id_information = user["user_id"]

        data_card = {
            "title": randomic_letters_uppercase(length=10),
            "user_id": user_id_information,
            "pan": pan_card,
            "expiry_mm": "01",
            "expiry_yyyy": "2999",
            "security_code": "123",
            "date": "12/12/2999",
        }
        req_card = requests.post(url=f"{URL_ADRESS}", data=json.dumps(data_card), headers=self.header)
        self.assertEqual(req_card.status_code, 201)

        data_card = {
            "title": randomic_letters_uppercase(length=10),
            "user_id": user_id_information,
            "pan": pan_card,
            "expiry_mm": "01",
            "expiry_yyyy": "2999",
            "security_code": "123",
            "date": "12/12/2999",
        }
        req_card = requests.post(url=f"{URL_ADRESS}", data=json.dumps(data_card), headers=self.header)
        self.assertEqual(req_card.status_code, 409)

    def test_create_new_card_without_title_in_json_body(self):
        data = {
            "user_id": generate_char_and_number_random(size=30),
            "pan": generate_random_number(16),
            "expiry_mm": "01",
            "expiry_yyyy": "2999",
            "security_code": generate_random_number(3),
            "date": "12/12/2999",
        }
        req_card = requests.post(url=f"{URL_ADRESS}", data=json.dumps(data), headers=self.header)
        self.assertEqual(req_card.status_code, 409)

    def test_create_new_card_without_pan_in_json_body(self):
        data = {
            "title": randomic_letters_uppercase(length=10),
            "user_id": generate_char_and_number_random(size=30),
            "expiry_mm": "01",
            "expiry_yyyy": "2999",
            "security_code": generate_random_number(3),
            "date": "12/12/2999",
        }
        req_card = requests.post(url=f"{URL_ADRESS}", data=json.dumps(data), headers=self.header)
        self.assertEqual(req_card.status_code, 409)

    def test_create_new_card_without_expiry_mm_in_json_body(self):
        data = {
            "title": randomic_letters_uppercase(length=10),
            "user_id": generate_char_and_number_random(size=30),
            "pan": generate_random_number(16),
            "expiry_yyyy": "2999",
            "security_code": generate_random_number(3),
            "date": "12/12/2999",
        }
        req_card = requests.post(url=f"{URL_ADRESS}", data=json.dumps(data), headers=self.header)
        self.assertEqual(req_card.status_code, 409)

    def test_create_new_card_without_expiry_yyyy_in_json_body(self):
        data = {
            "title": randomic_letters_uppercase(length=10),
            "user_id": generate_char_and_number_random(size=30),
            "pan": generate_random_number(16),
            "expiry_mm": "01",
            "security_code": generate_random_number(3),
            "date": "12/12/2999",
        }
        req_card = requests.post(url=f"{URL_ADRESS}", data=json.dumps(data), headers=self.header)
        self.assertEqual(req_card.status_code, 409)

    def test_create_new_card_without_security_code_in_json_body(self):
        data = {
            "title": randomic_letters_uppercase(length=10),
            "user_id": generate_char_and_number_random(size=30),
            "pan": generate_random_number(16),
            "expiry_mm": "01",
            "expiry_yyyy": "2999",
            "date": "12/12/2999",
        }
        req_card = requests.post(url=f"{URL_ADRESS}", data=json.dumps(data), headers=self.header)
        self.assertEqual(req_card.status_code, 409)

    def test_create_new_card_without_date_in_json_body(self):
        data = {
            "title": randomic_letters_uppercase(length=10),
            "user_id": generate_char_and_number_random(size=30),
            "pan": generate_random_number(16),
            "expiry_mm": "01",
            "expiry_yyyy": "2999",
            "security_code": generate_random_number(3),
        }
        req_card = requests.post(url=f"{URL_ADRESS}", data=json.dumps(data), headers=self.header)
        self.assertEqual(req_card.status_code, 409)

    def test_create_new_card_with_invalid_month_in_json_body(self):
        data = {
            "title": randomic_letters_uppercase(length=10),
            "user_id": generate_char_and_number_random(size=30),
            "pan": generate_random_number(16),
            "expiry_mm": "13",
            "expiry_yyyy": "2999",
            "security_code": generate_random_number(3),
            "date": "12/12/2999",
        }
        req_card = requests.post(url=f"{URL_ADRESS}", data=json.dumps(data), headers=self.header)
        self.assertEqual(req_card.status_code, 409)

    def test_create_new_card_with_invalid_year_in_json_body(self):
        data = {
            "title": randomic_letters_uppercase(length=10),
            "user_id": generate_char_and_number_random(size=30),
            "pan": generate_random_number(16),
            "expiry_mm": "01",
            "expiry_yyyy": "2020",
            "security_code": generate_random_number(3),
            "date": "12/12/2999",
        }
        req_card = requests.post(url=f"{URL_ADRESS}", data=json.dumps(data), headers=self.header)
        self.assertEqual(req_card.status_code, 409)

    def test_create_new_card_with_invalid_pan_lenght_in_json_body(self):
        data = {
            "title": randomic_letters_uppercase(length=10),
            "user_id": generate_char_and_number_random(size=30),
            "pan": generate_random_number(10),
            "expiry_mm": "01",
            "expiry_yyyy": "2999",
            "security_code": generate_random_number(3),
            "date": "12/12/2999",
        }
        req_card = requests.post(url=f"{URL_ADRESS}", data=json.dumps(data), headers=self.header)
        self.assertEqual(req_card.status_code, 409)

    def test_create_new_card_with_invalid_security_code_lenght_in_json_body(self):
        data = {
            "title": randomic_letters_uppercase(length=10),
            "user_id": generate_char_and_number_random(size=30),
            "pan": generate_random_number(16),
            "expiry_mm": "01",
            "expiry_yyyy": "2999",
            "security_code": generate_random_number(4),
            "date": "12/12/2999",
        }
        req_card = requests.post(url=f"{URL_ADRESS}", data=json.dumps(data), headers=self.header)
        self.assertEqual(req_card.status_code, 409)
