from django.test import TestCase
from surveys.models.survey_progress import SurveyProgress
from surveys.models.survey_details import SurveyDetails
from app.models.company_address import Address
from app.models import Company
from app.models.user import User
from projectapp.models.project import Project
from django.utils import timezone
from dateutil.relativedelta import relativedelta

now = datetime.datetime.now()


clsas TestSurveyProgressModel(TestCase):

    def setUp(self):
        
        address = Address.objects.create(
            street = 'North Kwabenya',
            city = 'Accra',
            region = 'Greater Accra',
            country = 'Ghana',
            postal_code= '3425'
        )
        

        company =  Company.objects.create(
            name = 'GetINNOtized',
            description = 'A software and data science company',
            address = address

        )

        self.randomUser = User.objects.create_user(
            firstname="kwasi",
            email="kwasi@example.com",
            othernames="amoh",
            password = 'Admin@me',
            company = self.company.id
        )

        project = Project.objects.create(
            name="PushInsights",
            description="Hello There",
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

    def test_survey_progress_instance_creation(self):
        reandom_survey_progress = SurveyProgress.objects.create(
            user = self.user,
            questions_completed = 47,
            survey = self.random_survey_details,
            is_completed = False,
            last_modified = now,
            is_current = True
        )
        self.assertEqual(reandom_survey_progress.questions_completed, 47)
