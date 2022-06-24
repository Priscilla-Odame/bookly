from projectapp.models.project import ProjectMember, ProjectMemberRole, Project
from app.models.company import Company
from app.models.user import User
from projectapp.serializers.project import ProjectMemberSerializer, ProjectMemberRoleSerializer, UpdateProjectMemberSerializer, ApproveRejectSerializer
from rest_framework import generics, permissions
from django.core.mail import send_mail
from django.conf import settings
from django.template import loader
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework.reverse import reverse
from django.template.loader import get_template
import os
from app.utils import Utils
from asgiref.sync import sync_to_async
import asyncio


class ProjectMemberAPI(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint to read, update or delete a single Project Member object"""
    serializer_class = ProjectMemberSerializer
    queryset = ProjectMember.objects.all()


class CreateProjectMemberAPI(generics.CreateAPIView):
    """API endpoint to create project member objects"""
    serializer_class = ProjectMemberSerializer

    async def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data.get('members'), many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        project = request.data.get('project')
        members = ProjectMember.objects.values('user__id',
                                               'user__firstname',
                                               'user__othernames',
                                               'user__email',
                                               'project__name',
                                               'project__description',
                                               'role__name',
                                               'access_status', 'is_active').filter(project=project)
        sender = request.user
        invitee_id = request.data.get('members')
        invitee = invitee_id[0]
        invitees = invitee['user']

        if invitees is not None:
            invitee_id_queryset = User.objects.get(pk=invitees)
        else:
            raise ValueError("Please submit a valid recepient email")

        if project is not None:
            name = Project.objects.get(pk=project)
        else:
            raise ValueError("Please submit a valid project key")

        domain = get_current_site(request).domain
        asyncio.create_task(Utils.send_invitation_mail(
            invitees, domain, sender, invitee_id_queryset, name))

        return Response({"project_id": project, "status": serializer.data, "members": members})


def validate_ids(data, field="id", unique=True):

    if isinstance(data, list):
        id_list = [int(x[field]) for x in data]
        if unique and len(id_list) != len(set(id_list)):
            raise ValidationError(
                "Multiple updates to a single {} found".format(field))

        return id_list

    return [data]


class UpdateProjectMemberAPI(generics.UpdateAPIView):
    """ API endpoint to update project member objects"""
    serializer_class = UpdateProjectMemberSerializer
    lookup_field = 'project_id'

    def get_serializer(self, *args, **kwargs):

        if isinstance(kwargs.get("data", {}), list):
            kwargs['many'] = True

        return super(UpdateProjectMemberAPI, self).get_serializer(*args, **kwargs)

    def get_queryset(self, ids=None):
        if ids:
            return ProjectMember.objects.filter(project=self.kwargs["project_id"], id__in=ids)

    def update(self, request, *args, **kwargs):
        ids = validate_ids(request.data)
        instances = self.get_queryset(ids=ids)
        serializer = self.get_serializer(
            instances, data=request.data, partial=False, many=True
        )

        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()


class RetrieveProjectMemberAPI(generics.RetrieveAPIView):
    serializer_class = ProjectMemberSerializer

    def get(self, request, *args, **kwargs):
        project_member = request.data.get('member_id')
        member = ProjectMember.objects.get(user=project_member)
        serialized = self.get_serializer(member)
        return Response(serialized.data)


class ProjectMemberRoleAPI(generics.CreateAPIView):
    """
    API endpoint to either create a projectMemberRole
    """
    serializer_class = ProjectMemberRoleSerializer
    queryset = ProjectMemberRole.objects


class MemberApproveRejectProject(generics.UpdateAPIView):
    queryset = ProjectMember.objects
    serializer_class = ApproveRejectSerializer
    permission_classes = [permissions.AllowAny, ]
    lookup_field = 'id'

    def get(self, request, id, uidb64, token):
        serializer = self.serializer_class()
        return Response(serializer.validate({"uidb64": uidb64, "token": token}))
