from rest_framework.test import APITestCase
from projectapp.models import Project, ProjectDashboard
from rest_framework import status
import datetime

now = datetime.datetime.now()


class TestProjectDashboardCreationAndListing(APITestCase):
    """
        This is a test of the CRUD implementation of the ProjectDashbobard model

    """

    def setUp(self):
        self.client.post(
            "/api/project/create_project", {
                "name": "Moses projects",
                "description": "Tits awesome",
                "is_deleted": False
            }
        )

    def test_dashboard_creation(self):
        """
        Test the endpoint for the creation of a ProjectDashboard object

        """
        project = Project.objects.get(name="Moses projects")

        url = "/api/dashboards/list_create_dashboards"
        payload = {
            "name": "Some Dashboard",
            "project": project.id,
            "is_active": True,
            "is_deleted": False
        }
        response = self.client.post(
            url,
            payload,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_listing_all_projectDashboards(self):
        """
            Test the endpoint for listing all ProjectDashboard objects

        """
        response = self.client.get(
            "/api/dashboards/list_create_dashboards", format="json"

        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestProjectDashboardUpdateAndRetrieveOne(APITestCase):

    def setUp(self):
        self.client.post(
            "/api/project/create_project", {
                "name": "Moses projects",
                "description": "Tits awesome",
                "is_deleted": False
            }
        )

        project = Project.objects.get(name="Moses projects")

        url = "/api/dashboards/list_create_dashboards"
        payload = {
            "name": "Some Dashboard",
            "project": project.id,
            "is_active": True,
            "is_deleted": False
        }
        self.client.post(
            url,
            payload,
            format="json"
        )

    def test_updating_project(self):
        """
            Test the endpoint for updating a ProjectDashboard object

        """

        project = Project.objects.get(name="Moses projects")

        payload = {
            "name": "Some Dashboard",
            "project": project.id,
            "is_active": True,
            "published_at": now,
            "is_deleted": False
        }
        dash_id = ProjectDashboard.objects.get(project=project).id

        response = self.client.put(
            f"/api/dashboard/{dash_id}",
            payload,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieving_a_dashboard(self):
        """
            Test the endpoint for reading a single ProjectDashboard object data

        """
        project = Project.objects.get(name="Moses projects")
        dash_id = ProjectDashboard.objects.get(project=project).id

        response = self.client.get(
            f"/api/dashboard/{dash_id}", format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestProjectDashboardDeletingOne(APITestCase):

    def setUp(self):
        self.client.post(
            "/api/project/create_project", {
                "name": "Moses projects",
                "description": "Tits awesome",
                "is_deleted": False
            }
        )

        project = Project.objects.get(name="Moses projects")
        url = "/api/dashboards/list_create_dashboards"
        payload = {
            "name": "Some Dashboard",
            "project": project.id,
            "is_active": True,
            "is_deleted": False
        }
        self.client.post(
            url,
            payload,
            format="json"
        )

    def test_deleting_a_dashboard(self):
        """
            Test the endpoint for flagging as deleted a ProjectDashboard object

        """
        project = Project.objects.get(name="Moses projects")
        dash_id = ProjectDashboard.objects.get(project=project).id
        response = self.client.delete(
            f"/api/dashboard/{dash_id}", format="json"
        )
        deleted_status = ProjectDashboard.all_objects.get(
            project=project).deleted_at

        self.assertNotEqual(deleted_status, None)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
