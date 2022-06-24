from rest_framework.test import APITestCase
from app.models import Project, User, FileUpload
import datetime

now = datetime.datetime.now()


class TestFileUploadCreation(APITestCase):
    """
    These are test cases for the CRUD implementation of File uploads
    """

    def setUp(self):

        project_url = "/api/project/create_project"
        project_payload = {
            "name": "ROGG",
            "description": "This is some decription"
        }
        response = self.client.post(
            project_url,
            project_payload,
            format="json"
        )

        User.objects.create(
            firstname="Philip",
            othernames="",
            email="philip@example.com",
        )

    def test_create_project_creation(self):
        project_id = Project.objects.get(name='ROGG').pk
        user_id = User.objects.get(firstname='Philip').pk

        with open('mediafiles/File/Philip_Owusu-Afriyie_.pdf', 'rb') as fp:
            response = self.client.post('/api/fileUpload/create', {
                "project": project_id,
                "user": user_id,
                "tittle": "Philip's file",
                "timestamp": now,
                "data_file": fp,
                "is_deleted": False,
            }, format='multipart')

            self.assertEqual(response.status_code, 201)


class TestReadingFileUploadDetails(APITestCase):
    """
    These are test cases for the CRUD implementation of File_uploadss
    """

    def setUp(self):

        project_url = "/api/project/create_project"
        project_payload = {
            "name": "ROGG",
            "description": "This is some decription"
        }
        response = self.client.post(
            project_url,
            project_payload,
            format="json"
        )

        User.objects.create(
            firstname="Philip",
            othernames="",
            email="philip@example.com",
        )

        project_id = Project.objects.get(name='ROGG').pk
        user_id = User.objects.get(firstname='Philip').pk

        with open('mediafiles/File/Philip_Owusu-Afriyie_.pdf', 'rb') as fp:
            response = self.client.post('/api/fileUpload/create', {
                "project": project_id,
                "user": user_id,
                "tittle": "Philip's file",
                "timestamp": now,
                "data_file": fp,
            }, format='multipart')

    def test_reading_all_file_uploadss(self):
        reports = self.client.get('/api/fileUploads', format="json")
        self.assertEqual(reports.status_code, 200)

    def test_reading_one_file_upload(self):
        project_id = Project.objects.get(name='ROGG').pk
        file_id = FileUpload.objects.get(project=project_id).id
        response = self.client.get(
            f"/api/fileUpload/{file_id}",
            format="json"
        )
        self.assertEqual(response.status_code, 200)
