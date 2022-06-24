from django.db import models
from app.models.Soft_deletion import SoftDeletionModel
from app.models.user import User
from surveys.models.survey_details import SurveyDetails
from django.utils import timezone


class SurveyProgress(SoftDeletionModel):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )

    questions_completed = models.IntegerField(
        blank=False, null=False
    )

    survey = models.ForeignKey(
        SurveyDetails,
        on_delete=models.PROTECT
    )

    is_completed = models.BooleanField(
        default=False
    )

    last_modified = models.DateTimeField(
        default=timezone.now
    )

    is_current = models.BooleanField(
        default=False,
    )
