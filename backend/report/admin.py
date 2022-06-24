from django.contrib import admin
from .models.report import Report
from app.admin_soft_deletion import SoftDeletionAdmin


class ReportAdmin(SoftDeletionAdmin):
    list_display = (
        'name',
        'description',
        'published_at',
        'project',
        'last_modified',
        'deleted_at',
    )


admin.site.register(Report, ReportAdmin)