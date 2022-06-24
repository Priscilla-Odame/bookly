from django.db import models
from app.models.Soft_deletion import SoftDeletionModel
from projectapp.models.project import Project
from django.utils import timezone


class SurveyDetails(SoftDeletionModel):
    name = models.CharField(
        max_length=100,
        null=False,
        unique=True
    )

    question_count = models.IntegerField(
        blank=False, null=False
    )

    description = models.CharField(
        max_length=500,
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.PROTECT,
        related_name='survey_project'
    )

    survey_deadline = models.DateTimeField(
        null=False,
        blank=False,
        default=None
    )

    published_at = models.DateTimeField(
        default=timezone.now
    )
