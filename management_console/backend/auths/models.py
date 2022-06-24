from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from datetime import date
from rest_framework_simplejwt.tokens import RefreshToken
from phonenumber_field.modelfields import PhoneNumberField
import uuid


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self,firstname, lastname, email, phone_number, password= None):
        """
        Create and save a User with the given email and password.
        """
        if not firstname:
            raise ValueError(_('User should have Firstname'))
        if not lastname:
            raise ValueError(_('User should have Lastname'))
        if not email:
            raise ValueError(_('User should have Email'))
        if not phone_number:
            raise ValueError(_('User should have Phone Number'))
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.firstname = firstname
        user.lastname = lastname
        user.phone_number = phone_number
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,firstname, lastname, email, phone_number, password= None):
        """
        Create and save a SuperUser with the given email and password.
        """

        if not firstname:
            raise ValueError(_('User should have Firstname'))
        if not lastname:
            raise ValueError(_('User should have Lastname'))
        if not email:
            raise ValueError(_('User should have Email'))
        if not phone_number:
            raise ValueError(_('User should have Phone Number'))
        if password is None:
            raise TypeError(_("User should have password"))

        user = self.create_user(
                email=self.normalize_email(email),
                firstname=firstname,
                lastname=lastname,
                phone_number = phone_number
            )
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user


    def create_staffuser(self,firstname, lastname, email, phone_number, password= None):

        if not firstname:
            raise ValueError(_('User should have Firstname'))
        if not lastname:
            raise ValueError(_('User should have Lastname'))
        if not email:
            raise ValueError(_('User should have Email'))
        if not phone_number:
            raise ValueError(_('User should have Phone Number'))
        if password is None:
            raise TypeError(_("User should have password"))

        user = self.create_user(
            email=self.normalize_email(email),
            firstname=firstname,
            lastname=lastname,
            phone_number = phone_number
        )
        user.set_password(password)
        user.firstname = firstname
        user.lastname = lastname
        user.phone_number = phone_number
        user.is_admin = False
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    email = models.EmailField(_('Email'), unique = True)
    password = models.CharField(max_length = 100)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    is_admin = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False )
    is_superuser = models.BooleanField(default = False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname','lastname','phone_number']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_refresh_token(self):
        refresh = RefreshToken.for_user(self)
        return  str(refresh)

    user_refresh_token = property(get_refresh_token)

    def get_access_token(self):
        refresh = RefreshToken.for_user(self)
        return str(refresh.access_token)
        
    user_access_token = property(get_access_token)

