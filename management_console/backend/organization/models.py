from django.db import models
import uuid
from django.contrib.auth.models import User



# Create your models here.

class OrganizationStatus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    updated_by = models.ForeignKey(User, null=False)
    updated_at = models.DateTimeField(auto_now=True)

class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    updated_by = models.ForeignKey(User, null=False)
    updated_at = models.DateTimeField(auto_now=True)

class Organization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    logo = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)
    status = models.ForeignKey(OrganizationStatus, null=False)
    updated_by = models.ForeignKey(User, null=False)
    updated_at = models.DateTimeField(auto_now=True)

class Contact(models.Model):
    ACTIVATED = '0'
    DEACTIVATED = '1'
    STATUS_CHOICES = [(ACTIVATED, 'Activated'), (DEACTIVATED, 'Deactivated'),]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    staff_member = models.ForeignKey(User, null=False)
    organization = models.ForeignKey(Organization, null=False)
    status = models.CharField(choices=STATUS_CHOICES, default=DEACTIVATED)
    updated_by = models.ForeignKey(User, null=False)
    updated_at = models.DateTimeField(auto_now=True)