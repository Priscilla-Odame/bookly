from django.contrib import admin
from projectapp.models.project import Project, ProjectDashboard, ProjectMember, ProjectMemberRole
from app.admin_soft_deletion import SoftDeletionAdmin
from django.contrib.contenttypes.models import ContentType
from django.utils.html import format_html
from django.urls import reverse
from app.models.company import Company

class ProjectAdmin(SoftDeletionAdmin):
    list_display = ('id',
                    'name',
                    'company',
                    'description',
                    'published_at',
                    'deleted_at'
                    )


class ProjectMemberRoleAdmin(SoftDeletionAdmin):
    list_display = ('id',
                    'name',
                    'deleted_at'
                    )


class ProjectMemberAdmin(SoftDeletionAdmin):
    list_display = ('id',
                    'user',
                    'project',
                    'role',
                    'approval_status',
                    'published_at',
                    'is_active',
                    'access_status',
                    'deleted_at'
                    )


class ProjectDashboardAdmin(SoftDeletionAdmin):
    list_display = ("id",
                    "name",
                    "project",
                    "is_active",
                    "published_at",
                    "deleted_at"
                    )


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectDashboard, ProjectDashboardAdmin)
admin.site.register(ProjectMemberRole, ProjectMemberRoleAdmin)
admin.site.register(ProjectMember, ProjectMemberAdmin)