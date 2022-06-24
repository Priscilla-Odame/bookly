from projectapp.models.project import Project, ProjectMember
from projectapp.serializers.project import ProjectSerializer, ProjectDetailsSerializer
from rest_framework import generics
from rest_framework.response import Response
from django.core.exceptions import ValidationError


class CreateProjectAPI(generics.CreateAPIView):
    """
    This endpoint is used to create new projects

    Sample Response:
    {
    "id": 1,
    "name": "Push Insights",
    "description": "This is a project that will allow companies to track their OKRs / KPIs",
    "is_deleted": false
}
    """

    serializer_class = ProjectSerializer
    queryset = Project.objects

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), list):
            kwargs['many'] = True

        return super(CreateProjectAPI, self).get_serializer(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        created_by = self.request.user

        if isinstance(request.data, list):
            for project in request.data:
                project['created_by'] = created_by
        else:
            raise ValidationError("Invalid Input")
        return super(CreateProjectAPI, self).post(request, *args, **kwargs)


class ListProjectAPI(generics.ListAPIView):
    """
    This endpoint is used to retrieve all existing projects

    Sample Response:
    [
    {
        "id": 1,
        "name": "Push Insights",
        "description": "This is a project that will allow companies to track their OKRs / KPIs",
        "is_deleted": false
    }
]

    """
    serializer_class = ProjectSerializer
    filterset_fields = ['name', 'description']
    search_fields = ['name', 'description']

    def get_queryset(self):
        user = self.request.user
        company = user.company.id
        return Project.objects.filter(company=company)


class RetrieveProjectAPI(generics.RetrieveAPIView):
    """
    This endpoint is used to retrieve a single existing project

    Sample Response:
    {
    "id": 1,
    "name": "Push Insights",
    "description": "This is a project that will allow companies to track their OKRs / KPIs",
    "is_deleted": false
}
    """
    serializer_class = ProjectDetailsSerializer
    queryset = Project.objects
    filterset_fields = ['name', 'description']
    search_fields = ['name', 'description']
    lookup_field = "id"

    def get(self, request, id):
        serializer = self.serializer_class()
        results = serializer.get_members({'project': id})
        return Response(results)


class UpdateProjectAPI(generics.UpdateAPIView):
    """
    This endpoint is used to update the details of a project

    Sample Response:

{
    "id": 1,
    "name": "Pull Insights",
    "description": "This is a project that will allow companies to track their OKRs / KPIs"
}
    """
    serializer_class = ProjectSerializer
    lookup_field = 'id'
    queryset = Project.objects


class DeleteProjectAPI(generics.DestroyAPIView):
    lookup_field = 'id'
    serializer_class = ProjectSerializer
    queryset = Project.objects
