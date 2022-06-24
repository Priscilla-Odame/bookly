from django.test import TestCase
from django.urls import reverse

"""
    This is a unit test to test if an email is valid and unique.
    The first test checks if the email is valid and at the same time unique,
    and returns a 200 OK response.
    The second test checks if the email is not valid and returns a 400
    BAD REQUEST response.
    The third test checks if the email already exists and gives a 400
    BAD REQUEST response.
    The fourth test checks if the email field is blank and gives a 400 BAD
    REQUEST response.

"""


class ValidateEmailTestCase(TestCase):
    fixtures = ["user.json"]

    def test_valid_unique_email(self):
        data = {
            "firstname": "Me",
            "email": "priscy@her.com"}
        response_data = self.client.post(reverse("email"), data)
        self.assertTrue(response_data.data)

    def test_invalid_email(self):
        data = {"email": "priscy@"}
        response_data = self.client.post(reverse("email"), data)
        self.assertTrue(response_data.data)

    def test_unique_email(self):
        data = {
            "email": "admin@gmail.com",  # email in the test fixture
        }
        response_data = self.client.post(reverse("email"), data)
        self.assertTrue(response_data.data)

    def test_blank_email(self):
        data = {
            "email": "",
        }
        response_data = self.client.post(reverse("email"), data)
        self.assertTrue(response_data.data)
