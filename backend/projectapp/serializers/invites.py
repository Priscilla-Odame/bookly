from rest_framework import serializers
from rest_framework.settings import api_settings
from projectapp.models.project import Project, ProjectDashboard, ProjectMember, ProjectMemberRole


class PendingInvitesSerializer(serializers.ModelSerializer):

    def get_members(self, attrs):
        # attrs = super().validate(attrs)
        members = ProjectMember.objects.values('user__firstname',
                                               'user__othernames',
                                               'user__email',
                                               'id',
                                               'role__name',
                                               'published_at',
                                               'access_status',
                                               'approval_status').filter(project=attrs['project'])
        project = Project.objects.values().get(id=attrs['project'])
        #return project
        return ({'project': project.name, "members": members})

    class Meta:
        model = ProjectMember
        fields = ('id',
                  'published_at',
                  'is_active',
                  'user',
                  'access_status',
                  'project',
                  'role',
                  'approval_status'
                  )
        read_only_fields = ('id', 'published_at','is_active', 'project',
                            'deleted_at', 'user','access_status','role')