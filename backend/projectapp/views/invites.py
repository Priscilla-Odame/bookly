from rest_framework import generics
from rest_framework.response import Response
from projectapp.serializers.invites import PendingInvitesSerializer
from projectapp.models.project import ProjectMember, ProjectMemberRole, Project
from app.models.user import User

class PendingInvitationsView(generics.ListAPIView):
    queryset = ''

    def get(self, request):
        data = [
            {
                "id": "4",
                "name": "Community Project",
                "description": "Description of Community Project",
                "invited_at" : "15-02-2021 09:30 am",
                "status" : "active"
            },
            {
                "id": "5",
                "name": "Rogg",
                "description": "Description of Rogg Project",
                "invited_at" : "15-02-2021 09:30 am",
                "status" : "active"
                
            }

        ]
        return Response(data)

# class PendingInvitationsView(generics.ListAPIView):
#     """
#     This endpoint is used to retrieve all existing projects

#     Sample Response:
#     [
#     {
#         "id": 1,
#         "name": "Push Insights",
#         "description": "This is a project that will allow companies to track their OKRs / KPIs",
#         "is_deleted": false
#     }
# ]

#     """
#     serializer_class = PendingInvitesSerializer
#     queryset = ProjectMember.objects
#     lookup_field = 'id'
#     filterset_fields = ['user','approval_status']

#     def get(self,request, *args, **kwargs):
#         user = request.data.get(queryset)
#         print(f'-----------{user}')
#         desc = user.project.description
#         data = [
#             {
#                 "id": "4",
#                 "name": "Community Project",
#                 "description": "Description of Community Project",
#                 "invited_at" : "15-02-2021 09:30 am",
#                 "status" : "active"   
#             }
#         ]
#         return Response(data)



#     #search_fields = ['name', 'description']

#     # def get_queryset(self):
#     #     user = self.request.user
#     #     company = user.company.id
#     #     member = ProjectMember.objects
#     #     return ProjectMember.objects.filter(approval_status=company)
