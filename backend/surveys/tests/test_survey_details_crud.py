from app.models import Company, User
from app.models.company_address import Address
from app.models.company import Company
from surveys.models.survey_details import SurveyDetails
from surveys.models.survey_progress import SurveyProgress
from rest_framework.test import APITestCase
from rest_framework.test import APIClient 
from django.utils import timezone
from dateutil.relativedelta import relativedelta
import json

now = datetime.datetime.now()


class TestSurveyDetailsCRUD(APITestCase):
    """
    Test cases for SurveyDetails CRUD endpoints
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
        
        self.project= Project.objects.create(
            name='Pull Insights',
            description='Hello There',
            company = self.company,
            published_at=now,
            status='Active'
            )

    def test_survey_details_creation(self):

        payload= {
            "name": "An awesome survey",
            "question_count": 77,
            "description": "For awesome people only",
            "survey_deadline": now += relativedelta(years=+1),
            "published_at": now,
            "project": self.project.id
                }

        response = self.client.post('surveys/create', payload, content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_updating_a_surveys_details(self):
        survey_details = SurveyDetails.objects.get(project = self.project.id)

        payload = {
            "name": "An awesome survey updated",
            "question_count": 77,
            "description": "Filled with more awesome queries",
            "survey_deadline": now += relativedelta(years=+1),
            "published_at": now,
            "project": survey_details.project
        }
        response = self.client.put(f'surveys/update/{survey_details.id}', payload, format='json')
        self.assertEqual(response.status_code, 200)

    def test_retrieving_a_surveys_details(self):
        survey_details = SurveyDetails.objects.get(project = self.project.id)


        response = self.client.get(f'surveys/{survey_details.id}')
        data = json.loads(response.content)
        survey_details_id = data[0]['id']
        self.assertEqual(survey_details_id, survey_details.id )

    def test_listing_survey_details(self):
        response = self.client.get('surveys')
        self.assertEqual(response.status_code, 200)

    def test_deleting_a_surveys_details(self):
        survey_details = SurveyDetails.objects.get(project = self.project.id)
        response = self.client.delete(f'surveys/remove/{survey_details.pk}', format='json')
        self.assertEqual(response.status_code, 204)

