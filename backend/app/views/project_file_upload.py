from django.contrib.admin.utils import lookup_field
from app.tasks import progress_upload
from app.models.file_upload import FileUpload
from app.serializers.project_file_upload import FileUploadSerializer
from projectapp.models.project import Project, ProjectMember
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from app.models.user import User
from django.shortcuts import get_object_or_404


class CreateProjectFileUploadAPIBeta(APIView):
    """
    API endpoint for creating project file_upload
    This endpoint no longer return response about the upload details
    but rather returns a task id to be used to track the progress of the upload
    Sample Response:

    {
        "progress_endpoint" : "cceacbc0-937e-494c-b774-2a3678870e88"
    }

    """

    def post(self, request, *args, **kwargs):
        upload_data = request.data
        project_instance = Project.objects.get(id=upload_data['project'])
        print(project_instance)
        user_instance = User.objects.get(email=upload_data['user'])
        print(user_instance)
        file = request.FILES['data_file']
        print(type(file))
        task = progress_upload.delay(file, 10000, upload_data, user_instance, project_instance, FileUpload)
        return Response({"progress_endpoint": 'celery-progress/' + task.task_id})


class CreateProjectFileUploadAPI(generics.CreateAPIView):
    """
    API endpoint for creating project a file_upload

    Sample Response:

{
    "id": 1,
    "title": "lnlnl",
    "timestamp": "2020-12-14T19:31:50.811580Z",
    "data_file": "https://pistorage01.blob.core.windows.net/media/GetInnotized/2/Python_-_List_Programming_Challenges_RlzdXpB.pdf",
    "file_size": "86.25 Kilobytes",
    "project": 2,
    "user": 1,
    "comment": "something"
}
    """

    serializer_class = FileUploadSerializer


class ListProjectFileUploadsAPI(generics.ListAPIView):
    """
    API endpoint for viewing all file_uploads of a particular project

    Sample Response:
[
    {
        "id": 4,
        "user": 1,
        "project": 1,
        "data_file": "https://pistorage01.blob.core.windows.net/media/File/Python_-_List_Programming_Challenges_etdzSXq.pdf",
        "title": "George's file",
        "timestamp": "2021-06-03T15:03:39.400804Z"
    }
]
    """
    serializer_class = FileUploadSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        user = self.request.user
        projects = ProjectMember.objects.values("project").filter(user=user)

        return FileUpload.objects.filter(project__in=projects).order_by("-timestamp")


class RetrieveProjectFileUploadDetailsAPI(generics.RetrieveAPIView):
    """
    API endpoint for reading a single project file_upload details

    Sample Response:
{
    "id": 4,
    "user": 1,
    "project": 1,
    "data_file": "https://pistorage01.blob.core.windows.net/media/File/Python_-_List_Programming_Challenges_etdzSXq.pdf",
    "title": "George's file",
    "timestamp": "2021-06-03T15:03:39.400804Z"
}
    """
    serializer_class = FileUploadSerializer

    def get_queryset(self):
        user = self.request.user
        file_id = self.kwargs.get('pk')
        file = FileUpload.objects.get(pk=file_id)
        projects = ProjectMember.objects.values(
            "project").filter(user=user, project=file.project)

        return FileUpload.objects.filter(project__in=projects)


class DeleteProjectUploadedFileAPI(generics.DestroyAPIView):
    """
    API endpoint to delete already uploaded project files from local/blob storage
    """
    serializer_class = FileUploadSerializer

    queryset = FileUpload.objects
    lookup_field = "pk"

    def get_queryset(self):
        user = self.request.user
        return FileUpload.objects.filter(user=user)

    # def get_queryset(self):
    #     user = self.request.user
    #     file_owner = get_object_or_404(FileUpload, user=user)
    #     return self.queryset.filter(user=file_owner)


class UpdateProjectUploadedFileAPI(generics.UpdateAPIView):
    """
    API endpoint for updating an uploaded project file details/content
{
    "id": 4,
    "user": 1,
    "project": 1,
    "data_file": "https://pistorage01.blob.core.windows.net/media/File/Python_-_List_Programming_Challenges_etdzSXq.pdf",
    "title": "George's file",
    "timestamp": "2021-06-03T15:03:39.400804Z"
}
    """
    queryset = FileUpload.objects
    serializer_class = FileUploadSerializer
    lookup_field = "pk"

    def get_queryset(self):
        user = self.request.user

        return FileUpload.objects.filter(user=user)
