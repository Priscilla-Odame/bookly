from django.db import models
from app.models.Soft_deletion import SoftDeletionModel


class Address(SoftDeletionModel):
    street = models.TextField(
        max_length=128,
        null=True
    )
    city = models.TextField(
        max_length=128,
    )
    region = models.TextField(
        'Region/Province',
        max_length=128,
    )
    country = models.TextField(
        max_length=128,
    )
    postal_code = models.TextField(
        max_length=128,
    )

    def __str__(self):
        return f'{self.street}, {self.city}, {self.region}, {self.country}, {self.postal_code},'
