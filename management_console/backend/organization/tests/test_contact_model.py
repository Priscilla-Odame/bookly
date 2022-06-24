from django.test import TestCase
from organization.models.organization import OrganizationStatus, Organization
from organization.models.contact import ContactStatus, ContactRole, Contact
from django.contrib.auth.models import User


class TestAdministratorModel(TestCase):

    def setUp(self):
        user = self.user = User.objects.create(
            first_name='Kwasi',
            password='password'
        )
        #
        # contact_updated_by_user = self.user = User.objects.create(
        #     first_name='Abena',
        #     password='password'
        # )

        contact_status = self.organization_status = ContactStatus.objects.create(
            name='active',
            updated_by=user
        )

        contact_role = self.organization_status = ContactRole.objects.create(
            name='Lead',
            updated_by=user
        )

        organization_status = self.organization_status = OrganizationStatus.objects.create(
            name='pending',
            updated_by=user
        )

        organization = self.organization = Organization.objects.create(
            name='Telefonica',
            logo='Telefonica.jpg',
            description='A software and data science company',
            updated_by=user,
            status=organization_status
        )

        self.contact = Contact.objects.create(
            staff_member=user,
            organization=organization,
            status=contact_status,
            role=contact_role,
            updated_by=user,

        )

    def test_contact_status_created(self):
        status = ContactStatus.objects.get(name='active')
        self.assertEqual(status.name, 'active')

    def test_contact_role_created(self):
        role = ContactRole.objects.get(name="Lead")
        self.assertEqual(role.name, "Lead")

    def test_contact_created(self):
        contact = Contact.objects.filter()
        self.assertEqual(contact.__len__(), 1)





