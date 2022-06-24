import json

from rest_framework.test import APITestCase
from projectapp.models import Project, ProjectMemberRole, ProjectMember
from app.models import User, Company
from app.models.company_address import Address
from rest_framework import status
import datetime
from rest_framework.test import APIClient


now = datetime.datetime.now()


class TestProjectMemberCreation(APITestCase):
    """
        This is a test of the CRUD implementation of the ProjectMember model

    """
    def setUp(self):
        self.client = APIClient()
        address = Address.objects.create(
            street='chale street',
            city='Accra',
            region='Greater-Accra',
            country='Ghana',
            postal_code='P.O.Box DC 131'
        )

        company = Company.objects.create(
            name='Silicon Valley',
            description='A company for software enthusiasts',
            address=address
        )

        User.objects.create_user(
            firstname="Moses",
            othernames="Wuniche",
            email="wuniche@gmail.com",
            company=company.id,
            password="moses123"
        )

        user = User.objects.create_user(
            firstname="Philip",
            othernames="Owusu-Afriyie",
            email="philip.afriyie@gmail.com",
            company=company.id,
            password="password"
        )

        project = Project.objects.create(
            name="Moses projects",
            description="Tits awesome",
            company=company,
            status='active'
        )

        role = ProjectMemberRole.objects.create(
            name="ProjectManager",
            description="Manage Projects"
        )

        ProjectMember.objects.create(
            user=user,
            project=project,
            project_member_role=role,
            is_active=False,
            access_status='invited'
        )

    def test_project_member_creation(self):
        """
        Test the endpoint for the creation of a ProjectMember
        """

        response = self.client.post(
            "/api/user/login",
            {"email": "wuniche@gmail.com", "password": "moses123"}
        )

        access_token = response.data["tokens"]["access"]

        user = User.objects.get(firstname='Moses')
        project = Project.objects.get(name='Moses projects')
        role = ProjectMemberRole.objects.get(name='ProjectManager')

        member_data = {
            "project": project.id,
            "members": [
                {
                    "user": user.id,
                    "project": project.id,
                    "project_member_role": role.id,
                    "is_active": True,
                    "access_status": "invited"
                }
            ]
        }

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + access_token)

        response = self.client.post(
            '/api/project/members/create',
            member_data,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_listing_all_projectMembers(self):
        """
            Test the endpoint for listing all ProjectMembers
        """

        response = self.client.post(
            "/api/user/login",
            {"email": "wuniche@gmail.com", "password": "moses123"}
        )
        access_token = response.data["tokens"]["access"]
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + access_token)

        project = Project.objects.get(name='Moses projects')

        response = self.client.get(
            f"/api/project/{project.id}",
            format="json"
        )
        self.assertEqual(len(response.data["members"]), 1)

    def test_updating_project_member_details(self):
        """
        Test the endpoint for the updating the details of a ProjectMember
        """

        response = self.client.post(
            "/api/user/login",
            {"email": "wuniche@gmail.com", "password": "moses123"}
        )
        access_token = response.data["tokens"]["access"]
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + access_token)

        user = User.objects.get(firstname='Philip')
        project = Project.objects.get(name='Moses projects')
        role = ProjectMemberRole.objects.get(name='ProjectManager')
        member = ProjectMember.objects.get(user=user)

        update_member = [
            {
                "id": member.id,
                "is_active": True,
                "access_status": "accepted",
                "user": user.id,
                "project_member_role": role.id

            },
        ]

        response = self.client.put(
            f"/api/project/{project.id}/members/update",
            update_member,
            format="json"
            )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
