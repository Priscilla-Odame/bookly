from app.models import User, Company
from projectapp.models.project import Project
from app.models.company_address import Address
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
import json
import datetime

now = datetime.datetime.now()


class TestProjectCRUD(APITestCase):
    """
    These are test cases for the CRUD implementation of Projects
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
            firstname='kwasi',
            email='kwasi@example.com',
            othernames='amoh',
            password = 'Admin@me',
            company = self.company
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

        self.project= Project.objects.create(
            name='Pull Insights',
            description='Hello There',
            company = self.company,
            published_at=now,
            status='Active'
            )
        
    
    def test_project_creation(self):
        """
            Testing the creation of a project
        """
        data ={
            'name': 'ROGG',
            'description': 'Testing ROGG project creation',
            'company': self.company,
            'published_at': now,
            'status': 'Active'
            }
        response = self.client.post('/api/project/create_project', data, content_type='application/json')
        self.assertEqual(response.status_code, 201)

        
    def test_updating_project(self):
        """
            Testing updating the details of a project
        """
        project_id = self.project.id

        payload = {
            "name": "Updated ROGG",
            "description": "New Testing ROGG project creation",
            'company': self.company.id,
            'published_at': now,
            'status': 'Active'
        }
        response = self.client.put(f'/api/project/{project_id}/update', payload, format='json')
        self.assertEqual(response.status_code, 200)

    
    def test_deleting_project(self):
        """
            Testing the deletion of a project
        """
        project = Project.objects.get(name='Pull Insights')
        response = self.client.delete(f'/api/project/{project.pk}/delete', format='json')
        self.assertEqual(response.status_code, 204)


    def test_get_projects(self):
        """
            Testing retrieving the details of a project
        """
        response = self.client.get('/api/projects')
        data = json.loads(response.content)
        project_name = data[0]['name']
        self.assertEqual(project_name, 'Pull Insights')



