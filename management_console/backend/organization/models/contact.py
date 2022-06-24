from django.db import models
import uuid
from auths.models import User
from .profile import Profile
from .organization import Organization
from .contactRole import ContactRole
from .contactStatus import ContactStatus
from phonenumber_field.modelfields import PhoneNumberField

class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    staff_member = models.ForeignKey(User, null=False, on_delete=models.PROTECT, related_name='+')
    organization = models.ForeignKey(Organization, null=False, on_delete=models.PROTECT)
    email = models.EmailField(null=False, unique=True)
    phone_number = PhoneNumberField(null=False, blank=False)
    profile = models.ForeignKey(Profile, null = True,blank = True, on_delete=models.CASCADE)
    status = models.ForeignKey(ContactStatus, null=False, on_delete=models.PROTECT)
    role = models.ForeignKey(ContactRole, null=False, on_delete=models.PROTECT)
    updated_by = models.ForeignKey(User, null=False, on_delete=models.PROTECT)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def name(self):        
        return '%s %s' %(self.staff_member.firstname, self.staff_member.lastname,)

    def __str__(self) -> str:
        return str(self.staff_member)