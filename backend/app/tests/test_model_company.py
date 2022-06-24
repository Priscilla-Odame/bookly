from django.test import TestCase
from app.models import Company
from app.models.company_address import Address

class TestCompanyModel(TestCase):
    def setUp(self):
       
        Address.objects.create(
            street = 'North Kwabenya',
            city = 'Accra',
            region = 'Greater Accra',
            country = 'Ghana',
            postal_code= '3425'
        )

    def test_address_created_successfully(self):
        address = Address.objects.get(city = 'Accra')
        self.assertEqual(address.street, 'North Kwabenya')

    def test_company_created_successfully(self):
        address = Address.objects.get(city = 'Accra')
        company =  Company.objects.create(
            name = 'GetINNOtized',
            description = 'A software and data science company',
            address = address

        )
        self.assertEqual(company.address.street, 'North Kwabenya')

