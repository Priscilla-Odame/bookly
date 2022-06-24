from django.test import TestCase
from app.models import FileUpload, Project, User


class TestFileUploadModel(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            name='PushInsights',
            description='Hello There'
        )
        self.user = User.objects.create(
            firstname='kwasi',
            email='kwasi@example.com',
            othernames='amoh'
        )

    def test_data_upload_created(self):
        data_upload = FileUpload.objects.create(
            project=self.project,
            user=self.user,
            tittle='Image',
            data_file='mediafiles/File/Philip_Owusu-Afriyie_.pdf'
        )
        data_upload.save()
        self.assertEqual(data_upload.project.name, self.project.name)
        self.assertEqual(data_upload.user.email, self.user.email)
