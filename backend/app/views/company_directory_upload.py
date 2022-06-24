from django.contrib.admin.utils import lookup_field

from app.models.company_directory_upload import CompanyDirectoryFilesUpload
from app.serializers.company_directory_upload import CompanyDirectoryFilesUploadSerializer
from projectapp.models.project import Project, ProjectMember
from rest_framework import generics
from rest_framework.response import Response
from app.models.user import User
from django.shortcuts import get_object_or_404
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.core.files.uploadhandler import FileUploadHandler


class CreateCompanyDirectoryUploadAPI(generics.CreateAPIView):
    """
    API endpoint for creating a Company file_upload

    Sample Response:

{"Directory files": [{
                "id": 3,
                "user": 4,
                "directory_name": "Some new directory by Misty",
                "data_file": "https://pistorage01.blob.core.windows.net/media/GetInnotized/4/azureLabSetup.pdf",
                "file_size": "1.8 MB",
                "timestamp": "2021-06-09T19:33:04.835268Z"
            },{
                "id": 3,
                "user": 4,
                "directory_name": "Some new directory by Misty",
                "data_file": "https://pistorage01.blob.core.windows.net/media/GetInnotized/4/azureLabSetup.pdf",
                "file_size": "1.8 MB",
                "timestamp": "2021-06-09T19:33:04.835268Z"
            } ]
}
    """

    serializer_class = CompanyDirectoryFilesUploadSerializer

    def post(self, request):

        serializer = self.serializer_class(
            data=request.data,  context={'request': request})
        serializer.is_valid(raise_exception=True)

        return Response(serializer.validated_data)


class ListCompanyDirectoryUploadsAPI(generics.ListAPIView):
    """
    API endpoint for viewing all Company file_uploads

    Sample Response:
[
    {
        "id": 3,
        "user": 4,
        "title": "This is an awesome file",
        "data_file": "https://pistorage01.blob.core.windows.net/media/GetInnotized/4/azureLabSetup.pdf",
        "comment": "Well it should be awesome...",
        "timestamp": "2021-06-09T19:33:04.835268Z"
    }
]
    """
    serializer_class = CompanyDirectoryFilesUploadSerializer
    lookup_field = 'pk'
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend,)
    search_fields = ["title", "user__firstname"]

    def get_queryset(self):
        user = self.request.user

        return CompanyDirectoryFilesUpload.objects.filter(user=user).order_by("-timestamp")


class RetrieveCompanyUploadedDirectoryDetailsAPI(generics.RetrieveAPIView):
    """
    API endpoint for reading a Company single file_upload details

    Sample Response:
{
    "id": 3,
    "user": 4,
    "title": "This is an awesome file",
    "data_file": "https://pistorage01.blob.core.windows.net/media/GetInnotized/4/azureLabSetup.pdf",
    "comment": "Well it should be awesome...",
    "timestamp": "2021-06-09T19:33:04.835268Z"
}
    """
    serializer_class = CompanyDirectoryFilesUploadSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        user = self.request.user

        return CompanyDirectoryFilesUpload.objects.filter(user=user)


class DeleteCompanyUploadedDirectoryAPI(generics.DestroyAPIView):
    """
    API endpoint to delete already uploaded Company files from local/blob storage
    """
    serializer_class = CompanyDirectoryFilesUploadSerializer

    queryset = CompanyDirectoryFilesUpload.objects
    lookup_field = "pk"

    def get_queryset(self):
        user = self.request.user
        return CompanyDirectoryFilesUpload.objects.filter(user=user)


class UpdateCompanyUploadedDirectoryAPI(generics.UpdateAPIView):
    """
    API endpoint for updating an uploaded company file details/content
{
    "id": 2,
    "user": 2,
    "title": "lnlnl",
    "data_file": "https://pistorage01.blob.core.windows.net/media/GetInnotized/2/Python_-_List_Programming_Challenges.pdf",
    "comment": "Changed",
    "file_size": "86.25 Kilobytes",
    "timestamp": "2021-06-21T22:15:20.342044Z"
}
    """
    serializer_class = CompanyDirectoryFilesUploadSerializer
    queryset = CompanyDirectoryFilesUpload.objects
    lookup_field = "pk"

    def get_queryset(self):
        user = self.request.user

        return CompanyDirectoryFilesUpload.objects.filter(user=user)
