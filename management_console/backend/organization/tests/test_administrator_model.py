from django.test import TestCase
from organization.models.administrator import AdministratorStatus, Administrator
from organization.models.organization import OrganizationStatus, Organization
from django.contrib.auth.models import User


class TestAdministratorModel(TestCase):

    def setUp(self):

        user = self.user = User.objects.create(
            first_name='kwabena',
            password='password'
        )

        admin_status = self.organization_status = AdministratorStatus.objects.create(
            name='active',
            updated_by=user
        )

        status = self.organization_status = OrganizationStatus.objects.create(
            name='pending',
            updated_by=user
        )

        organization = self.organization = Organization.objects.create(
            name='Telefonica',
            logo='Telefonica.jpg',
            description='A software and data science company',
            updated_by=user,
            status=status
        )

        self.administrator = Administrator.objects.create(
            name='Kwame Mintah',
            email='kwame.mintah@gmail.com',
            organization=organization,
            phone_number='0205639875',
            role='Captain',
            status=admin_status,
            updated_by=user,

        )

    def test_admin_status_created (self):
        status = AdministratorStatus.objects.get(name='active')
        self.assertEqual(status.name, 'active')

    def test_organization_created(self):
        organization = Organization.objects.get(name="Telefonica")
        self.assertEqual(organization.logo, "Telefonica.jpg")

    def test_administrator_created(self):
        admin = Administrator.objects.get(email='kwame.mintah@gmail.com')
        self.assertEqual(admin.role, 'Captain')





