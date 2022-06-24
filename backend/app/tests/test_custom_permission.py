from app.models import User, Company, Project, ProjectMember, ProjectMemberRole
from app.models.company_address import Address
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
import json 
import datetime

now = datetime.datetime.now()

class TestUserPermission(APITestCase):

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

        self.user = User.objects.create_user(
            firstname="kwasi",
            email="kwasi@example.com",
            othernames="amoh",
            company = self.company.id,
            password="password"
        )
        self.project = Project.objects.create(
            name="PushInsights",
            description="Hello There",
            company = self.company,
            created_at=now,
            status='Active'
        )
        self.role = ProjectMemberRole.objects.create(
            name="Administrator",
            description="Manage Projects"
        )

    def test_user_is_authenticated(self):
        project_member = ProjectMember.objects.create(
            user=self.user,
            project = self.project,
            project_member_role = self.role
            )

        response = self.client.get('/api/companies')
        data = json.loads(response.content)
        company_name = data[0]["name"]
        self.assertEqual(company_name, 'GetINNOtized')

    def test_authorized_user(self):

        data = {
            'email':'kwasi@example.com',
            'password':'password'
        }
        response = self.client.post(
            "/api/user/login",
            data,
            format='json'
        )
        access_token = response.data['tokens']['access']

        project_member = ProjectMember.objects.create(
            user=self.user,
            project = self.project,
            project_member_role = self.role
            )


        update_member = [
            {
                "id": project_member.id,
                "is_active": True,
                "access_status": "accepted",
                "user": self.user.id,
                "project_member_role": self.role.id

            },
        ]

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + access_token)

        response = self.client.put(
            f"/api/project/{self.project.id}/members/update",
            update_member,
            format="json"
            )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthorized_user(self):
        
        project_member = ProjectMember.objects.create(
            user=self.user,
            project = self.project,
            project_member_role = self.role
            )


        update_member = [
            {
                "id": project_member.id,
                "is_active": True,
                "access_status": "accepted",
                "user": self.user.id,
                "project_member_role": self.role.id

            },
        ]

        response = self.client.put(
            f"/api/project/{self.project.id}/members/update",
            update_member,
            format="json"
            )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        

        