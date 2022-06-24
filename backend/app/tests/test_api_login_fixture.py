from app.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status


# Create your tests here.
class UserLoginTestCase(TestCase):
    fixtures = ["user.json"]

    def test_wrongpassword_wrongemail(self):
        user = User.objects.get(pk=1)
        data = {
            "email": "priscy@his.com",
            "password": "hello",
        }
        returned_values = self.client.post(reverse("login"), data)
        self.assertEqual(returned_values.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(user.othernames, "Odame")

    def test_wrongpassword_correctemail(self):
        user = User.objects.get(pk=1)
        data = {
            "email": "admin@gmail.com",
            "password": "hello",
        }
        returned_values = self.client.post(reverse("login"), data)
        self.assertEqual(returned_values.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(user.othernames, "Odame")

    def test_correctpassword_wrongemail(self):
        # Create user
        user = User.objects.get(pk=1)
        data = {
            "email": "priscy@his.com",
            "password": "admin",
        }
        returned_values = self.client.post(reverse("login"), data)
        self.assertEqual(returned_values.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(user.othernames, "Odame")
