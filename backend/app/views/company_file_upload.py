from django.contrib.admin.utils import lookup_field
from app.tasks import progress_upload
from app.models.company_file_upload import CompanyFileUpload
from app.serializers.company_file_upload import CompanyFileUploadSerializer
from projectapp.models.project import Project, ProjectMember
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models.user import User
from django.shortcuts import get_object_or_404
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from azure.storage.blob import BlockBlobService
from app.models.custom_azure import PublicMediaAzureStorage

class CreateCompanyFileUploadAPIBeta(APIView):
    """
    API endpoint for creating company  file_upload
    This endpoint no longer return response about the upload details
    but rather returns a task id to be used to track the progress of the upload
    Sample Response:

    {
        "progress_endpoint" : "cceacbc0-937e-494c-b774-2a3678870e88"
    }

    """

    def post(self, request, *args, **kwargs):
        upload_data = request.data
        # company_instance = CompanyFileUpload.objects.get(id=upload_data['company'])
        user_instance = User.objects.get(id=upload_data['user'])
        file = request.FILES['data_file']
        task = progress_upload.delay(file, 10000, upload_data, user_instance, model_instance=CompanyFileUpload)
        return Response({"progress_endpoint": 'celery-progress/' + task.task_id})
        #  celery-progress/5e027727-755e-46b5-bf74-93a2572d4d07

class CreateCompanyFileUploadAPI(generics.CreateAPIView):
    """
    API endpoint for creating a Company file_upload

    Sample Response:

{
    "id": 3,
    "user": 4,
    "data_file": "https://pistorage01.blob.core.windows.net/media/GetInnotized/4/azureLabSetup.pdf",
    "comment": "Well it should be awesome...",
    "timestamp": "2021-06-09T19:33:04.835268Z"
}
    """

    serializer_class = CompanyFileUploadSerializer

    # def get_serializer(self, *args, **kwargs):
    #     if isinstance(kwargs.get("data", {}), list):
    #         kwargs["many"] = True

    #     return super(CreateCompanyFileUploadAPI, self).get_serializer(*args, **kwargs)

    # def post(self, request):
    #     # print(f'====================== {request.data}')

    #     serializer = self.serializer_class(
    #         data=request.data, context={'request': request})
    #     serializer.is_valid(raise_exception=True)
    #     # serializer.save()
    #     return Response(serializer.validated_data)

    # def post(self, request, *args, **kwargs):
    #     upload_data = request.data
    #     user_instance = User.objects.get(email=upload_data['user'])
    #     uploaded_file_instance = CompanyFileUpload(name=upload_data['name'], user=user_instance, data_file=upload_data['file_data'], )


    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        credentials = request.user.company.azure_details
        data_file = request.FILES['data_file']
        block_blob_service = BlockBlobService( account_name=credentials.azure_account_name, account_key=credentials.azure_account_key)
        container_name = 'media'
        block_blob_service.create_container(container_name)
        fs = PublicMediaAzureStorage(
                        account_name=credentials.azure_account_name,
                        account_key=credentials.azure_account_key,
                        azure_container=container_name,
                        location=f'{request.user.id}',
                        custom_domain=f'{credentials.azure_account_name}.blob.core.windows.net',
                        overwrite_files=False
                        )
        filename = fs.save(data_file.name, data_file)
        uploaded_file_url = fs.url(data_file.name)
        response = {
            'id': serializer.data['id'],
            'name': filename,
            'user': serializer.data['user'],
            'data_file': uploaded_file_url,
            'comment': serializer.data['comment'],
            'file_size': serializer.data['file_size'],
            'timestamp': serializer.data['timestamp']
        }
        return Response(response,status=status.HTTP_201_CREATED,headers=headers)



class ListCompanyFileUploadsAPI(generics.ListAPIView):
    """
    API endpoint for viewing all Company file_uploads

    Sample Response:
[
    {
        "id": 3,
        "user": 4,
        "data_file": "https://pistorage01.blob.core.windows.net/media/GetInnotized/4/azureLabSetup.pdf",
        "comment": "Well it should be awesome...",
        "timestamp": "2021-06-09T19:33:04.835268Z"
    }
]
    """
    serializer_class = CompanyFileUploadSerializer
    lookup_field = 'pk'
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend,)
    search_fields = ["title", "user__firstname"]

    def get_queryset(self):
        user = self.request.user

        return CompanyFileUpload.objects.filter(user=user).order_by("-timestamp")


class RetrieveCompanyFileUploadDetailsAPI(generics.RetrieveAPIView):
    """
    API endpoint for reading a Company single file_upload details

    Sample Response:
{
    "id": 3,
    "user": 4,
    "data_file": "https://pistorage01.blob.core.windows.net/media/GetInnotized/4/azureLabSetup.pdf",
    "comment": "Well it should be awesome...",
    "timestamp": "2021-06-09T19:33:04.835268Z"
}
    """
    serializer_class = CompanyFileUploadSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        user = self.request.user

        return CompanyFileUpload.objects.filter(user=user)


class DeleteCompanyUploadedFileAPI(generics.DestroyAPIView):
    """
    API endpoint to delete already uploaded Company files from local/blob storage
    """
    serializer_class = CompanyFileUploadSerializer

    queryset = CompanyFileUpload.objects
    lookup_field = "pk"

    def get_queryset(self):
        user = self.request.user
        return CompanyFileUpload.objects.filter(user=user)


class UpdateCompanyUploadedFileAPI(generics.UpdateAPIView):
    """
    API endpoint for updating an uploaded company file details/content
{
    "id": 2,
    "user": 2,
    "data_file": "https://pistorage01.blob.core.windows.net/media/GetInnotized/2/Python_-_List_Programming_Challenges.pdf",
    "comment": "Changed",
    "file_size": "86.25 Kilobytes",
    "timestamp": "2021-06-21T22:15:20.342044Z"
}
    """
    serializer_class = CompanyFileUploadSerializer
    queryset = CompanyFileUpload.objects
    lookup_field = "pk"

    def get_queryset(self):
        user = self.request.user

        return CompanyFileUpload.objects.filter(user=user)



class CreateCompanyFileUploadView(viewsets.ModelViewSet):
    """
    API endpoint for creating a Company file_upload

    Sample Response:

{
    "id": 3,
    "user": 4,
    "data_file": "https://pistorage01.blob.core.windows.net/media/GetInnotized/4/azureLabSetup.pdf",
    "comment": "Well it should be awesome...",
    "timestamp": "2021-06-09T19:33:04.835268Z"
}
    """

    serializer_class = CompanyFileUploadSerializer
    queryset = CompanyFileUpload.objects

    # def get_serializer(self, *args, **kwargs):
    #     if isinstance(kwargs.get("data", {}), list):
    #         kwargs["many"] = True

    #     return super(CreateCompanyFileUploadAPI, self).get_serializer(*args, **kwargs)

    # def post(self, request):
    #     # print(f'====================== {request.data}')

    #     serializer = self.serializer_class(
    #         data=request.data, context={'request': request})
    #     serializer.is_valid(raise_exception=True)
    #     # serializer.save()
    #     return Response(serializer.validated_data)

    # def post(self, request, *args, **kwargs):
    #     upload_data = request.data
    #     user_instance = User.objects.get(email=upload_data['user'])
    #     uploaded_file_instance = CompanyFileUpload(name=upload_data['name'], user=user_instance, data_file=upload_data['file_data'], )


    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        credentials = request.user.company.azure_details
        data_file = request.FILES['data_file']
        block_blob_service = BlockBlobService( account_name=credentials.azure_account_name, account_key=credentials.azure_account_key)
        container_name = 'media'
        block_blob_service.create_container(container_name)
        fs = PublicMediaAzureStorage(
                        account_name=credentials.azure_account_name,
                        account_key=credentials.azure_account_key,
                        azure_container=container_name,
                        location=f'{request.user.id}',
                        custom_domain=f'{credentials.azure_account_name}.blob.core.windows.net',
                        overwrite_files=False
                        )
        self.filename = fs.save(data_file.name, data_file)
        self.uploaded_file_url = fs.url(data_file.name)
        response = {
            'id': serializer.data['id'],
            'name': self.filename,
            'user': serializer.data['user'],
            'data_file': self.uploaded_file_url,
            'comment': serializer.data['comment'],
            'file_size': serializer.data['file_size'],
            'timestamp': serializer.data['timestamp']
        }
        return Response(response,status=status.HTTP_201_CREATED,headers=headers)


    def list(self, request,filename,uploaded_file_url, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        response = {

            'id': serializer.data[0],
            'name': filename,
            'user': serializer.data[2],
            'data_file': uploaded_file_url,
            'comment': serializer.data[3],
            'file_size': serializer.data[4],
            'timestamp': serializer.data[5]
        }
        return Response(response)