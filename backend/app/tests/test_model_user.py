from django.test import TestCase
from app.models import User, Company
from app.models.company_address import Address
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class TestUserModel(TestCase):
    def setUp(self):

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
        User.objects.create(
            firstname="kwasi",
            email="kwasi@example.com",
            othernames="amoh",
            company = self.company
        )
        User.objects.create(
            firstname="jennifer",
            email="jennifer@example.com",
            othernames="bempong",
            company = self.company
        )

    def test_user_created(self):
        user1 = User.objects.get(firstname="kwasi")
        user2 = User.objects.get(email="jennifer@example.com")
        self.assertEqual(user1.email, "kwasi@example.com")
        self.assertEqual(user2.firstname, "jennifer")

    def test_create_user_with_blank_othernames(self):
        user = User.objects.create(
            firstname="priscilla",
            email="priscilla@example.com",
            othernames="",
            password="password",
            company = self.company
        )
        self.assertEqual(user.othernames, "")

    def test_create_user_with_invalid_email(self):
        email = "mojo#example,com"
        data = {'firstname': 'kojo', 'email': email,
                'othernames': 'amoh', 'password': 'password','company': self.company.id}
        #self.assertEqual(validate_email(email), False)
        with self.assertRaises(ValidationError):
            User.objects.create_user(**data)

    def test_create_user_without_firstname(self):
        user = User(
            email="kojo@example.com",
            othernames="amoh",
            password="password",
            company = self.company
        )
        self.assertRaises(ValidationError, user.full_clean)

    def test_create_user_with_valid_credentials(self):
        user = User.objects.create(
            firstname="kofi",
            email="kofi@example.com",
            othernames="amoh",
            password="password",
            company = self.company
        )
        self.assertEqual(user.firstname, 'kofi')
        self.assertEqual(user.email, 'kofi@example.com')
        self.assertEqual(user.othernames, 'amoh')
