from unittest import TestCase
import requests
import json

from config import HOST, PORT
from digital_account.blueprints.utils.generateRandomValues import randomic_letters_uppercase, generate_random_number
from digital_account.blueprints.utils.generateRandomValues import generate_char_and_number_random

URL_ADRESS = f"http://{HOST}:{PORT}/account/cards"


class ViewAccountCardsAPI(TestCase):
    header = {'content-type': 'application/json'}

    def test_status_code_page_with_get(self):
        # Title: Access the page and check the status Code
        # step 1: Access the page and verify the status_code of the page
        # Expected Result: It should return the status_code = 200
        req_get = requests.get(url=URL_ADRESS)
        self.assertEqual(req_get.status_code, 200)

    def test_create_new_card_and_verify_it_on_cards_page(self):
        # Title: Create a new user in the API Person and verify the same user in the API friends
        # step 1: Create a new user in the API Person, and verify its created sucessfully.
        # step 2: Check the API friends and verify the users created and check if the user created
        #       in step 1 is on API friends.
        # Expected Result: The user created must be in API friends.
        first_name = randomic_letters_uppercase(length=10)
        user_id = ""

        data = {
            "first_name": first_name,
            "last_name": randomic_letters_uppercase(length=20),
            "birthday": "01/01/1999",
            "password": generate_char_and_number_random(size=30),
            "username": generate_char_and_number_random(size=30),
        }
        req_post = requests.post(url=f"http://{HOST}:{PORT}/account/person", data=json.dumps(data), headers=self.header)
        self.assertEqual(req_post.status_code, 201)

        req_get = requests.get(url=f"http://{HOST}:{PORT}/account/friends")
        for user in req_get.json():
            if user["first_name"] == first_name:
                user_id = user["user_id"]
                break

        pan = generate_random_number(16)
        data_card = {
            "title": randomic_letters_uppercase(length=10),
            "user_id": user_id,
            "pan": pan,
            "expiry_mm": "01",
            "expiry_yyyy": "2999",
            "security_code": "123",
            "date": "12/12/2999",
        }
        req_card = requests.post(url=f"http://{HOST}:{PORT}/account/card", data=json.dumps(data_card), headers=self.header)
        self.assertEqual(req_card.status_code, 201)

        req_get = requests.get(url=URL_ADRESS)
        for card in req_get.json():
            if card["pan"] == pan:
                self.assertEqual(card["pan", pan])
                return



