from django.test import TestCase
from projectapp.models.project import (Project, ProjectDashboard, ProjectMember,
                        ProjectMemberRole)
from app.models import User, Company
from app.models.company_address import Address
import datetime

now = datetime.datetime.now()


class TestProjectModel(TestCase):
    def setUp(self):

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
        Project.objects.create(
            name="PushInsights",
            description="Hello There",
            company = self.company,
            published_at=now,
            status='Active'
        )

    def test_project_created(self):
        project = Project.objects.get(name="PushInsights")
        self.assertEqual(project.name, "PushInsights")
        self.assertEqual(project.description, "Hello There")


class TestProjectDashboard(TestCase):
    def setUp(self):

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
        Project.objects.create(
            name="PushInsights",
            description="Hello There",
            company = self.company,
            published_at=now,
            status='Active'
        )

    def test_project_dashboard_created(self):
        project = Project.objects.get(name="PushInsights")
        project_dash = ProjectDashboard.objects.create(
            name="Push Dashboard",
            project=project,

        )
        self.assertEqual(project_dash.name, "Push Dashboard")


class TestProjectMemberRole(TestCase):
    def setUp(self):
        ProjectMemberRole.objects.create(
            name="Admin"
        )

    def test_project_member_role_created(self):
        project_member_role = ProjectMemberRole.objects.get(
            name="Admin"
        )
        self.assertEqual(project_member_role.name, "Admin")


class TestProjectMember(TestCase):

    def setUp(self):

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

        User.objects.create(
            firstname="kwasi",
            email="kwasi@example.com",
            othernames="amoh",
            company = self.company
        )
        Project.objects.create(
            name="PushInsights",
            description="Hello There",
            company = self.company,
            published_at=now,
            status='Active'
        )
        ProjectMemberRole.objects.create(
            name="Admin"
        )

    def test_project_member_created(self):
        user = User.objects.get(firstname="kwasi")
        project = Project.objects.get(name="PushInsights")
        project_member_role = ProjectMemberRole.objects.get(
            name="Admin")
        project_member = ProjectMember.objects.create(
            user=user,
            project = project,
            role = project_member_role
            )
        self.assertEqual(project_member.user.firstname, "kwasi")
