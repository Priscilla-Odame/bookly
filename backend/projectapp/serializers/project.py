from abc import ABC
from rest_framework import serializers
from rest_framework.settings import api_settings
from projectapp.models.project import Project, ProjectDashboard, ProjectMember, ProjectMemberRole
from app.models.user import User
from app.serializers.support.fields import CurrentProjectDefault, ModelObjectField
from django.utils import timezone
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from rest_framework.utils import html
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from rest_framework.reverse import reverse
from app.utils import token_generator


class BulkCreateProjectSerializer(serializers.ListSerializer, ABC):

    def create(self, validated_data):

        result = [self.child.create(attrs) for attrs in validated_data]

        try:
            self.child.Meta.model.objects.bulk_create(result)
        except IntegrityError as e:
            raise ValidationError(e)

        return result


class ProjectMemberRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMemberRole
        fields = "__all__"
        read_only_fields = ('deleted_at',)


class ProjectMemberSerializer(serializers.ModelSerializer):
    # role = ProjectMemberRoleSerializer()

    # def create(self, validated_data):
    #     role = validated_data.pop('role')
    #     new_role = ProjectMemberRole.objects.create(**role,)
    #     new_projectmember = ProjectMember.objects.create(**validated_data, role=new_role)

    #     return new_projectmember

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
        read_only_fields = ('deleted_at', 'id', 'access_status','approval_status')


class UpdateProjectMemberListSerializerMixin(object):

    def to_internal_value(self, data):
        """
        overwritten to prevent queryset validation error
        """
        if html.is_html_input(data):
            data = html.parse_html_list(data)

        if not isinstance(data, list):
            message = self.error_messages['not_a_list'].format(
                input_type=type(data).__name__
            )
            raise ValidationError({
                api_settings.NON_FIELD_ERRORS_KEY: [message]
            }, code='not_a_list')

        if not self.allow_empty and len(data) == 0:
            if self.parent and self.partial:
                raise SkipField()

            message = self.error_messages['empty']
            raise ValidationError({
                api_settings.NON_FIELD_ERRORS_KEY: [message]
            }, code='empty')

        ret = []
        errors = []

        for item in data:
            try:
                self.child.instance = self.instance.get(
                    id=item['id']) if self.instance else None
                self.child.initial_data = item
                validated = self.child.run_validation(item)
            except ValidationError as exc:
                errors.append(exc.detail)
            else:
                ret.append(validated)
                errors.append({})

        if any(errors):
            raise ValidationError(errors)
        return ret


class UpdateProjectMemberListSerializer(UpdateProjectMemberListSerializerMixin, serializers.ListSerializer):

    def update(self, instances, validated_data):

        instance_hash = {index: instance for index,
                         instance in enumerate(instances)}
        result = [
            self.child.update(instance_hash[index], attrs)
            for index, attrs in enumerate(validated_data)
        ]
        writable_fields = [
            x
            for x in self.child.Meta.fields
            if x not in self.child.Meta.read_only_fields
        ]

        try:
            self.child.Meta.model.objects.bulk_update(result, writable_fields)
        except IntegrityError as e:
            raise ValidationError(e)
        return result


class UpdateProjectMemberSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        instance.access_status = validated_data['access_status']
        instance.is_active = validated_data['is_active']
        instance.role = validated_data['role']

        if isinstance(self._kwargs['data'], dict):
            instance.save()

        return instance

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
        read_only_fields = ('id', 'published_at', 'project',
                            'deleted_at', 'user','approval_status')
        list_serializer_class = UpdateProjectMemberListSerializer



class ProjectSerializer(serializers.ModelSerializer):
    created_by = ModelObjectField()

    def create(self, validated_data):
        instance = Project(**validated_data)

        if isinstance(self._kwargs["data"], dict):
            instance.save()

        return instance

    class Meta:
        model = Project

        fields = (
            'id',
            'name',
            'company',
            'description',
            'published_at',
            'status',
            'created_by',
        )
        read_only_fields = ('id', 'published_at', 'created_by')
        list_serializer_class = BulkCreateProjectSerializer


class ProjectDetailsSerializer(serializers.ModelSerializer):

    def get_members(self, attrs):
        attrs = super().validate(attrs)
        members = ProjectMember.objects.values('user__firstname',
                                               'user__othernames',
                                               'user__email',
                                               'id',
                                               'role__name',
                                               'published_at',
                                               'access_status',
                                               'approval_status').filter(
            project=attrs['project'])
        project = Project.objects.values().get(id=attrs['project'])
        # return project
        return ({'project': project, "members": members})


class ProjectDashboardSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectDashboard
        fields = "__all__"
        read_only_fields = ('deleted_at',)


class ApproveRejectSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        instance.approval_status = validated_data['approval_status']

        if 'approval_status' in validated_data:
            instance.save()

        return instance

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