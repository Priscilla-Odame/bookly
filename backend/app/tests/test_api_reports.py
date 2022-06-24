from django.urls import reverse
from rest_framework import status
from app.models import Company, User
from app.models.company_address import Address
from rest_framework.test import APITestCase
from rest_framework.test import APIClient 

"""
        This is an integration test to check for the json response when a report is requested for

"""


class EmbeddedReportsTestCase(APITestCase):

    def setUp(self):

        self.client = APIClient()

        self.address = Address.objects.create(
            street = 'North Kwabenya',
            city = 'Accra',
            region = 'Greater Accra',
            country = 'Ghana',
            postal_code= '3425'
        )
        self.company = Company.objects.create(
            name = 'GetINNOtized',
            description = 'A software and data science company',
            address = self.address

        )

        User.objects.create_user(
            firstname="kwasi",
            email="kwasi@example.com",
            othernames="amoh",
            password = 'Admin@me',
            company = self.company.id
        )

        data = {
            'email':'kwasi@example.com',
            'password':'Admin@me'
        }
        response = self.client.post(
            '/api/user/login',
            data,
            format = 'json'
        )
        self.access_token = response.data['tokens']['access']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.access_token)


    def test_get_embedded_parameters(self):
        """
        Verify that the get embedded report Parameters API works as expected
        """
        url = reverse("report")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token_id', response.json())
