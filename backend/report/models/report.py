from django.db import models
from app.models.Soft_deletion import SoftDeletionModel
from projectapp.models.project import Project


class Report(SoftDeletionModel):

    @property
    def current_version(self):
        from .report_version import ReportVersion
        try:
            latest_version = ReportVersion.objects.filter(report__id=self.id).latest('last_modified')
        except ReportVersion.DoesNotExist:
            latest_version = ReportVersion(is_active=True, report=self)
            latest_version.save()
        return latest_version

    name = models.CharField(
        'Report Name',
        max_length=100,
        null=False,
        blank=False,
        unique=True
    )

    description = models.TextField(
        'Report Description'
    )

    project = models.ForeignKey(
        Project,
        null=False,
        blank=False,
        on_delete=models.PROTECT
    )
    published_at = models.DateField(
        auto_now_add=True
    )
    last_modified = models.DateField(
        auto_now_add=True
    )
    class Meta:
        unique_together = [['project', 'name']]

    def __str__(self):
        project_name = self.project.name
        report_name = self.name
        return f''' {project_name} - {report_name}'''
