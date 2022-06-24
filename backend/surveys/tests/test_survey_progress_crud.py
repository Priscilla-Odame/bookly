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

class TestSurveyProgressCRUD(APITestCase):
    """
    Test cases for SurveyProgress CRUD endpoints
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
        
        project= Project.objects.create(
            name='Pull Insights',
            description='Hello There',
            company = self.company,
            published_at=now,
            status='Active'
            )

        self.random_survey_details = SurveyDetails.objects.create(
            name = 'A random survey for testing',
            question_count = 77,
            description = 'Nothing important',
            project = project,
            published_at = now,
            survey_deadline =  now += relativedelta(years=+1)
        )

    def test_survey_progress_creation(self):

        payload= {
            "user": self.user.id,
            "questions_completed": 47,
            "survey": self.survey.id,
            "is_completed": False,
            "last_modified": now,
            "is_current": True
                }

        response = self.client.post('surveys/progress/create', payload, content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_updating_a_surveys_progress(self):
        survey_progress =  SurveyProgress.objects.get(user = self.user.id)

        payload = {
            "user": self.user.id,
            "questions_completed": 77,
            "survey": self.survey.id,
            "is_completed": True,
            "last_modified": now,
            "is_current": True
        }
        response = self.client.put(f'surveys/progress/update/{survey_progress}', payload, format='json')
        self.assertEqual(response.status_code, 200)

    def test_retrieving_a_surveys_progress(self):
        survey_progress = SurveyProgress.objects.get(user = self.user.id)

        response = self.client.get(f'surveys/progress/{survey_progress.id}')
        data = json.loads(response.content)
        questions_completed = data[0]['questions_answered']
        self.assertEqual(questions_completed, survey_progress.questions_completed)

    def test_listing_surveys_progress(self):
        response = self.client.get('surveys/progress')
        self.assertEqual(response.status_code, 200)

    def test_deleting_a_surveys_progress(self):
        survey_progress = SurveyProgress.objects.get(user = self.user.id)
        response = self.client.delete(f'surveys/progress/remove/{survey_progress.pk}', format='json')
        self.assertEqual(response.status_code, 204)