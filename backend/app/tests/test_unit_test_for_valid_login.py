import json
from app.models import User
from rest_framework.test import APITestCase
from django.test import Client

# making reference to custom user model
# User = get_user_model()


class ValidUserLoginTestCase(APITestCase):

    """
    This test is to assert for a valid login scenario
    To do so a new user registration test case will
    be created, after which the successfully created
    new user will be used to test the login endpoint
    for a valid login sinario
    """

    # A new user is singned up
    def test_register_new_user(self):
        userdata = {
            "firstname": "Moses",
            "othernames": "wuniche",
            "email": "moses@gmail.com",
            "password": "moses123"
        }

        response = self.client.post("/api/user/signup/", userdata)
        self.assertEqual(response.status_code, 200)

        # create and save user for testing

    def setUp(self):
        # User.objects.get()
        # creating temp user to use for testing
        user = User.objects.create_user(
            firstname="Moses",
            othernames="wuniche",
            email="wuniche@gmail.com",
            password="moses123"
        )
        # test registred user valid login

    def test_valid_login(self):
        response = self.client.post(
            "/api/user/login",
            {"email": "wuniche@gmail.com", "password": "moses123"}
        )
        self.assertEqual(response.status_code, 200)
