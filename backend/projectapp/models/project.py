from django.db import models
from django.utils import timezone

from app.models.user import User
from app.models.Soft_deletion import SoftDeletionModel
from app.models.company import Company


class Project(SoftDeletionModel):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        unique=True
    )
    description = models.CharField(
        max_length=500
    )
    company = models.ForeignKey(
        Company,
        null=False,
        blank=False,
        default=None,
        related_name='company_project',
        on_delete=models.PROTECT
    )
    published_at = models.DateTimeField(
        default=timezone.now
    )
    status = models.CharField(
        max_length=100,
        default='invited'
    )
    created_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.name


class ProjectDashboard(SoftDeletionModel):
    name = models.CharField(
        max_length=100
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.PROTECT,
    )
    is_active = models.BooleanField(
        default=True
    )
    published_at = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


class ProjectMemberRole(SoftDeletionModel):
    ADMINISTRATOR = 'Admin'
    MEMBER = 'Member'
    ROLE_CHOICES = [
        (ADMINISTRATOR, 'Admin'),
        (MEMBER, 'Member'),
    ]
    name = models.CharField(
        max_length=13,
        choices = ROLE_CHOICES,
        default = MEMBER,
    )

    def __str__(self):
        return self.name


class ProjectMember(SoftDeletionModel):
    STATUS = [
    ('0', 'Pending Approval'),
    ('1', 'Approved'),
    ('2', 'Rejected')
    ]
    user = models.ForeignKey(
        User,
        default=None,
        related_name='user',
        on_delete=models.PROTECT
    )
    project = models.ForeignKey(
        Project,
        default=None,
        related_name='members',
        on_delete=models.PROTECT
    )
    role = models.ForeignKey(
        ProjectMemberRole,
        related_name='project_member_role',
        on_delete=models.PROTECT
    )
    published_at = models.DateField(
        auto_now_add=True
    )
    is_active = models.BooleanField(
        default=False
    )
    access_status = models.CharField(
        max_length=100,
        default='invited'
    )
    approval_status = models.CharField(
        choices=STATUS,
        default='0',
        max_length=2
    )

    class Meta:
        unique_together = [['user', 'project']]

    def __str__(self):
        project_name = self.project.name
        first_name = self.user.firstname
        last_name = self.user.othernames
        return f''' {project_name}  - {first_name} {last_name}'''
