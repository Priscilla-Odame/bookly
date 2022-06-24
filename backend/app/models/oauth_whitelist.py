from django.db import models
from django.contrib.postgres.fields import ArrayField
from app.models.company import Company
from app.models.Soft_deletion import SoftDeletionModel


class CompaniesWhitelist(SoftDeletionModel):

    name = models.CharField(
        max_length=100
    )

    domain_names = ArrayField(
        models.CharField(max_length=100, blank=True)
    )

    company = models.ForeignKey(
        Company,
        null=False,
        blank=False,
        on_delete=models.PROTECT
    )
