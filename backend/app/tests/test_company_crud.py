from app.models import Company, User
from app.models.company_address import Address
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework.test import APIClient 
import json

class TestCompanyCRUD(APITestCase):
    """
    These are test cases for the CRUD implementation of Companies
    """
    
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
        
    
    def test_company_creation(self):
        """
            Testing the creation of a company
        """

        data = {
            'name': 'FairPointers',
            'description': 'Full stack developers wih great minds',
            'address': {
                'street': 'North Kwabenya',
                'city': 'Accra',
                'region':  'Greater Accra',
                'country': 'Ghana',
                'postal_code': '3425'
            }
        }

        response = self.client.post('/api/company/create', data, format='json')
        self.assertEqual(response.status_code, 201)

        
    def test_updating_company(self):
        """
            Testing updating the details of a company
        """
        company_id = self.company.id

        payload ={
            'id':company_id,
            'name': 'Azubi FairPointers',
            'description': ' Azubi Full stack developers wih great minds',
            'address': {
                'street': 'North Kwabenya',
                'city': 'Accra',
                'region':  'Greater Accra',
                'country': 'Ghana',
                'postal_code': '3425'
            }
        }

        response = self.client.put(f'api/company/{company_id}/update', payload, format='json')
        self.assertEqual(response.status_code, 200)

    
    def test_deleting_company(self):
        """
            Testing the deletion of a company
        """
        company = Company.objects.get(name='GetINNOtized')
        response = self.client.delete(f'api/company/{company.pk}/delete', format="json")
        self.assertEqual(response.status_code, 204)


    def test_get_companies(self):
        """
            Testing retrieving the details of a company
        """
        response = self.client.get('/api/companies')
        data = json.loads(response.content)
        company_name = data[0]["name"]
        self.assertEqual(company_name, 'GetINNOtized')