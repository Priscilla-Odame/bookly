from auths.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete =models.CASCADE )
    profile_pic = models.ImageField(null=True,blank=True,upload_to="profile/")


    def __str__(self):
        return str(self.user)