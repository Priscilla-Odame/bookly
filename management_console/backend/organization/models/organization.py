from django.db import models
import uuid
from auths.models import User
from .organizationStatus import OrganizationStatus
class Organization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    logo = models.ImageField(null=False,blank=False,upload_to="logo/")
    description = models.CharField(max_length = 200)
    status = models.ForeignKey(OrganizationStatus, null=False, on_delete=models.PROTECT)
    updated_by = models.ForeignKey(User, null=False, on_delete=models.PROTECT)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
