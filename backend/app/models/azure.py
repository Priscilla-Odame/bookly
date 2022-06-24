from django.db import models
from app.models.Soft_deletion import SoftDeletionModel


class AzureDetails(SoftDeletionModel):
    azure_account_name = models.CharField(
        max_length=128,
        null=True
    )
    azure_account_key = models.CharField(
        max_length=350,
    )

    def __str__(self):
        return f'{self.azure_account_name}'