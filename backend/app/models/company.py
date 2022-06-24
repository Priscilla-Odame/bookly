from django.db import models
from app.models.company_address import Address
from app.models.azure import AzureDetails
from app.models.Soft_deletion import SoftDeletionModel


class Company(SoftDeletionModel):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        unique=True
    )
    description = models.CharField(
        max_length=500
    )
    published_at = models.DateField(
        auto_now_add=True
    )
    address = models.ForeignKey(
        Address,
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    azure_details = models.OneToOneField(
    AzureDetails,
    null=True,
    blank=True,
    on_delete=models.PROTECT
)


    def __str__(self):
        return self.name
