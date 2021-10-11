from unittest import TestCase
import requests
import json

from config import HOST, PORT
from digital_account.blueprints.utils.generateRandomValues import randomic_letters_uppercase
from digital_account.blueprints.utils.generateRandomValues import generate_char_and_number_random

URL_ADRESS = f"http://{HOST}:{PORT}/account/person"


class ViewAccountPersonAPI(TestCase):
    header = {'content-type': 'application/json'}

    def test_page_status_code_with_get(self):
        # Title: Access the page and check the status Code
        # step 1: Access the page and verify the status_code of the page
        # Expected Result: It should return the status_code = 405 (method not allowed)
        req_get = requests.get(url=URL_ADRESS)
        self.assertEqual(req_get.status_code, 405)

    def test_create_new_user_without_user_available_in_database(self):
        # Title: Create a new user without other same username in database
        # step 1: Check the username in database
        # step 2: Create a new user with brand new username
        # Expected Result: The user should be create sucessfully, with status_code = 201
        data = {
            "first_name": randomic_letters_uppercase(length=10),
            "last_name": randomic_letters_uppercase(length=20),
            "birthday": "01/01/1999",
            "password": generate_char_and_number_random(size=30),
            "username": generate_char_and_number_random(size=30),
        }
        req_post = requests.post(url=URL_ADRESS, data=json.dumps(data), headers=self.header)
        self.assertEqual(req_post.status_code, 201)

    def test_create_new_user_with_a_username_in_database(self):
        # Title: Create a new user with other same username in database
        # step 1: Check the username available in database
        # step 2: Create a new user with brand new username
        # Expected Result: The user shouldn't be created, the page should return the status_code = 409
        username = generate_char_and_number_random(size=30)
        data = {
            "first_name": randomic_letters_uppercase(length=10),
            "last_name": randomic_letters_uppercase(length=20),
            "birthday": "01/01/1999",
            "password": generate_char_and_number_random(size=30),
            "username": username,
        }
        req_post = requests.post(url=URL_ADRESS, data=json.dumps(data), headers=self.header)
        self.assertEqual(req_post.status_code, 201)
        req_post = requests.post(url=URL_ADRESS, data=json.dumps(data), headers=self.header)
        self.assertEqual(req_post.status_code, 409)

    def test_create_new_user_without_first_name_in_json_body(self):
        # Title: Create a new user without the "first_name" in the body of Json POST.
        # step 1: Create a POST JSON and send it to the URL (/account/person)
        # step 2: Send it and verify the error. It shouldn't be created.
        # Expected Result: The user shouldn't be created without the parameter "first_name"
        data = {
            "last_name": randomic_letters_uppercase(length=20),
            "birthday": "01/01/1999",
            "password": generate_char_and_number_random(size=30),
            "username": generate_char_and_number_random(size=30),
        }
        req_post = requests.post(url=URL_ADRESS, data=json.dumps(data), headers=self.header)
        self.assertEqual(req_post.status_code, 409)

    def test_create_new_user_without_last_name_in_json_body(self):
        # Title: Create a new user without the "last_name" in the body of Json POST.
        # step 1: Create a POST JSON and send it to the URL (/account/person)
        # step 2: Send it and verify the error. It shouldn't be created.
        # Expected Result: The user shouldn't be created without the parameter "last_name"
        data = {
            "first_name": randomic_letters_uppercase(length=10),
            "birthday": "01/01/1999",
            "password": generate_char_and_number_random(size=30),
            "username": generate_char_and_number_random(size=30),
        }
        req_post = requests.post(url=URL_ADRESS, data=json.dumps(data), headers=self.header)
        self.assertEqual(req_post.status_code, 409)

    def test_create_new_user_without_birthday_in_json_body(self):
        # Title: Create a new user without the "birthday" in the body of Json POST.
        # step 1: Create a POST JSON and send it to the URL (/account/person)
        # step 2: Send it and verify the error. It shouldn't be created.
        # Expected Result: The user shouldn't be created without the parameter "birthday"
        data = {
            "first_name": randomic_letters_uppercase(length=10),
            "last_name": randomic_letters_uppercase(length=20),
            "password": generate_char_and_number_random(size=30),
            "username": generate_char_and_number_random(size=30),
        }
        req_post = requests.post(url=URL_ADRESS, data=json.dumps(data), headers=self.header)
        self.assertEqual(req_post.status_code, 409)

    def test_create_new_username_without_password_in_json_body(self):
        # Title: Create a new user without the "password" in the body of Json POST.
        # step 1: Create a POST JSON and send it to the URL (/account/person)
        # step 2: Send it and verify the error. It shouldn't be created.
        # Expected Result: The user shouldn't be created without the parameter "password"
        data = {
            "first_name": randomic_letters_uppercase(length=10),
            "last_name": randomic_letters_uppercase(length=20),
            "birthday": "01/01/1999",
            "username": generate_char_and_number_random(size=30),
        }
        req_post = requests.post(url=URL_ADRESS, data=json.dumps(data), headers=self.header)
        self.assertEqual(req_post.status_code, 409)

    def test_create_new_username_without_username_in_json_body(self):
        # Title: Create a new user without the "username" in the body of Json POST.
        # step 1: Create a POST JSON and send it to the URL (/account/person)
        # step 2: Send it and verify the error. It shouldn't be created.
        # Expected Result: The user shouldn't be created without the parameter "username"
        data = {
            "first_name": randomic_letters_uppercase(length=10),
            "last_name": randomic_letters_uppercase(length=20),
            "birthday": "01/01/1999",
            "password": generate_char_and_number_random(size=30),
        }
        req_post = requests.post(url=URL_ADRESS, data=json.dumps(data), headers=self.header)
        self.assertEqual(req_post.status_code, 409)
