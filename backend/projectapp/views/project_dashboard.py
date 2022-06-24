from projectapp.models.project import ProjectDashboard, Project
from projectapp.serializers.project import ProjectDashboardSerializer
from rest_framework import generics
from rest_framework import permissions


class ListCreateProjectDashboardsAPI(generics.ListCreateAPIView):
    """API endpoint to either create a project dashboard or
     list all dashboards depending on the methods (POST or GET)

     Sample Response:
     {
    "id": 1,
    "name": "Adding a new project dashboard",
    "is_active": true,
    "published_at": "2020-12-14",
    "is_deleted": false,
    "project": 2
}
    """
    serializer_class = ProjectDashboardSerializer

    def get_queryset(self):
        user = self.request.user
        company_id = user.company.id
        project_ids = Project.objects.values('id').filter(company=company_id)
        return ProjectDashboard.objects.filter(project__in=project_ids)


class ProjectDashboardAPI(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint to read, update and delete a single dashboard object"""
    serializer_class = ProjectDashboardSerializer
    queryset = ProjectDashboard.objects
