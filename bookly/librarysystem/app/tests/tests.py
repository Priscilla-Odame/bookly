from django.test import TestCase
from .models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class TestUserModel(TestCase):
    def setUp(self):

        User.objects.create(
            firstname='kwasi',
            lastname='asamoah'
            email='kwasi@example.com',
            username='Kwasi',
            date_of_birth='04-02-2003'
        )
        User.objects.create(
            firstname='jennifer',
            lastname='asamoah'
            email='jennifer@example.com',
            username='jenny',
            date_of_birth='05-02-2003'

    def test_user_created(self):
        user1 = User.objects.get(firstname='kwasi')
        user2 = User.objects.get(email='jennifer@example.com')
        self.assertEqual(user1.email, 'kwasi@example.com')
        self.assertEqual(user2.firstname, 'jennifer')

    def test_create_user_with_blank_lastname(self):
        user = User.objects.create(
            firstname='priscilla',
            lastname='',
            email='priscilla@example.com',
            username='Prissy',
            date_of_birth='05-02-2003',
            password="password"
        )
        self.assertEqual(user.lastname, '')

    def test_create_user_with_invalid_email(self):
        email = "mojo#example,com"
        data = {
            'firstname': 'kojo',
            'email': email,
            'lastname': 'amoh',
            'username': 'Kojo',
            'date_of_birth': '05-02-2003',
            'password': 'password'
            }
        #self.assertEqual(validate_email(email), False)
        with self.assertRaises(ValidationError):
            User.objects.create_user(**data)

    def test_create_user_without_firstname(self):
        user = User(
            email='kojo@example.com',
            lastname='amoh',
            username='Kojo',
            date_of_birth='05-02-2003',
            password='password',
        )
        self.assertRaises(ValidationError, user.full_clean)

    def test_create_user_with_valid_credentials(self):
        user = User.objects.create(
            firstname="kofi",
            email="kofi@example.com",
            lastname="amoh",
            username='Kofi',
            date_of_birth='05-02-2003',
            password="password"
        )
        self.assertEqual(user.firstname, 'kofi')
        self.assertEqual(user.email, 'kofi@example.com')
        self.assertEqual(user.lastname, 'amoh')
