from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

"""
        This is an integration test to check for the json response when an
        email is

        1. Valid and Unique
        2. Invalid
        3. Not Unique
        4. Email field is blank

"""


class ValidateEmailTestCase(APITestCase):
    fixtures = ["user.json"]

    def test_valid_and_unique_email(self):

        url = reverse("email")
        data = {"email": "priscy@her.com"}
        response = self.client.post(url, data, format="json")
        expected_response = {
            "message": "Email is valid and available",
            "status_code": 200,
        }
        self.assertDictEqual(expected_response, response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valid_email(self):

        url = reverse("email")
        data = {"email": "priscy@her"}
        response = self.client.post(url, data, format="json")
        expected_response = "Enter a valid email address."
        expected_status_code = 400
        self.assertEqual(response.status_code, expected_status_code)
        self.assertEqual(response.data.get("email")[0], expected_response)

    def test_unique_email(self):

        url = reverse("email")
        data = {"email": "admin@gmail.com"}  # Email exists in the fixture
        response = self.client.post(url, data, format="json")
        expected_response = "user with this Email already exists."
        expected_status_code = 400
        self.assertEqual(response.status_code, expected_status_code)
        self.assertEqual(response.data.get("email")[0], expected_response)

    def test_failure_blank_email(self):

        url = reverse("email")
        data = {"email": ""}
        response = self.client.post(url, data, format="json")
        expected_response = "This field may not be blank."
        expected_status_code = 400
        self.assertEqual(response.status_code, expected_status_code)
        self.assertEqual(response.data.get("email")[0], expected_response)
