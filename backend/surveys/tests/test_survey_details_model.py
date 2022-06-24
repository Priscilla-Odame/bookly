from django.test import TestCase
from surveys.models.survey_details import SurveyDetails
from app.models.company_address import Address
from app.models import Company
from projectapp.models.project import Project
from django.utils import timezone
from dateutil.relativedelta import relativedelta

now = datetime.datetime.now()


clsas TestSurveyDetailsModel(TestCase):

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

        project = Project.objects.create(
            name="PushInsights",
            description="Hello There",
            company = self.company,
            published_at=now,
            status='Active'
        )

    def test_survey_details_instance_creation(self):
        random_survey_details = SurveyDetails.objects.create(
            name = 'A random survey for testing',
            question_count = 77,
            description = 'Nothing important',
            project = project,
            published_at = now,
            survey_deadline =  now += relativedelta(years=+1)
        )
        self.assertEqual(random_survey_details.description, 'Nothing important')

