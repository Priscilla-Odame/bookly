from django.db import models
import uuid
from auths.models import User
from phonenumber_field.modelfields import PhoneNumberField
from .organization import Organization
from .profile import Profile

# Create your models here.

class AdministratorStatus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    updated_by = models.ForeignKey(User, null=False, on_delete=models.PROTECT)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

class Administrator(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    email = models.EmailField(null=False, unique=True)
    organization = models.ForeignKey(Organization, null=False, on_delete=models.PROTECT)
    phone_number = PhoneNumberField(null=False, blank=False)
    profile = models.ForeignKey(Profile, null = True,blank = True, on_delete=models.CASCADE)
    role = models.CharField(max_length = 200)
    status = models.ForeignKey(AdministratorStatus, null=False, on_delete=models.PROTECT)
    updated_by = models.ForeignKey(User, null=False, on_delete=models.PROTECT)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


    
