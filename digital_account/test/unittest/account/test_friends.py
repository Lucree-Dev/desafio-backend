from unittest import TestCase
import requests
import json

from config import HOST, PORT
from digital_account.blueprints.utils.generateRandomValues import randomic_letters_uppercase
from digital_account.blueprints.utils.generateRandomValues import generate_char_and_number_random

URL_ADRESS = f"http://{HOST}:{PORT}/account/friends"


class ViewAccountFriendsAPI(TestCase):
    header = {'content-type': 'application/json'}

    def test_status_code_page_with_get(self):
        # Title: Access the page and check the status Code
        # step 1: Access the page and verify the status_code of the page
        # Expected Result: It should return the status_code = 200
        req_get = requests.get(url=URL_ADRESS)
        self.assertEqual(req_get.status_code, 200)

    def test_create_new_user_and_verify_the_user_in_person(self):
        # Title: Create a new user in the API Person and verify the same user in the API friends
        # step 1: Create a new user in the API Person, and verify its created sucessfully.
        # step 2: Check the API friends and verify the users created and check if the user created
        #       in step 1 is on API friends.
        # Expected Result: The user created must be in API friends.
        first_name = randomic_letters_uppercase(length=10)
        find_user = False
        data = {
            "first_name": first_name,
            "last_name": randomic_letters_uppercase(length=20),
            "birthday": "01/01/1999",
            "password": generate_char_and_number_random(size=30),
            "username": generate_char_and_number_random(size=30),
        }
        req_post = requests.post(url=f"http://{HOST}:{PORT}/account/person", data=json.dumps(data), headers=self.header)
        self.assertEqual(req_post.status_code, 201)

        req_get = requests.get(url=URL_ADRESS)
        for user in req_get.json():
            if user["first_name"] == first_name:
                find_user = True
                self.assertEqual(user["first_name"], first_name)
                break

        assert find_user

