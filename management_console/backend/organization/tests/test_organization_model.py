from django.test import TestCase
from organization.models.organization import Organization, OrganizationStatus
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class TestOrganizationModel(TestCase):
    def setUp(self):

        user = self.user = User.objects.create(
            first_name='kwabena',
            password='password'
        )

        status = self.organization_status = OrganizationStatus.objects.create(
            name='active',
            updated_by=user
        )

        self.organization = Organization.objects.create(
            name='Telefonica',
            logo='Telefonica.jpg',
            description='A software and data science company',
            updated_by=user,
            status=status
        )

    def test_status_created (self):
        status = OrganizationStatus.objects.get(name='active')
        self.assertEqual(status.updated_by.first_name,'kwabena')

    def test_organization_created(self):
        organization = Organization.objects.get(name="Telefonica")
        self.assertEqual(organization.logo, "Telefonica.jpg")





