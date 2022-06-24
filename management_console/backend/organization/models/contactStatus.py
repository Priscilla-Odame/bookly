from django.db import models
from auths.models import User
import uuid

class ContactStatus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    updated_by = models.ForeignKey(User, null=False, on_delete=models.PROTECT)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name