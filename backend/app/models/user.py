from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.validators import validate_email
from app.models.company import Company
from django.db.models.signals import post_save
from django.dispatch import receiver
from app.services.send_email import Services


class UserManager(BaseUserManager):

    def create_user(self, firstname, email, othernames, company, password=None):
        if firstname is None:
            raise TypeError("Users should have firstname")
        if email is None:
            raise TypeError("User should have an email")
        if company is None:
            raise TypeError("Users must have a company associated.")
        else:
            validate_email(email)

        user = self.model(
            email=self.normalize_email(email),
            company=company
        )
        user.firstname = firstname
        user.othernames = othernames
        user.set_password(password)
        return user

    def create_superuser(self, firstname, othernames, company, email, password=None):

        if firstname is None:
            raise TypeError("Users should have firstname")
        if password is None:
            raise TypeError("Users should have password")
        if company is None:
            raise TypeError("Users must have a company associated.")

        company_instance = Company.objects.get(id=company)
        user = self.create_user(
            email=self.normalize_email(email),
            firstname=firstname,
            othernames=othernames,
            company=company_instance
        )
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, firstname, othernames, company, password=None):

        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not firstname:
            raise ValueError("User must have a first name")
        if not othernames:
            raise ValueError("User must have a last name")
        if company is None:
            raise TypeError("Users must have a company associated.")

        user = self.create_user(
            email=self.normalize_email(email),
            firstname=firstname,
            othernames=othernames,
            company=company
        )
        user.set_password(password)
        user.firstname = firstname
        user.othernames = othernames
        user.is_admin = False
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    # To be adjusted
    password = models.CharField(
        'Password',
        max_length=128,
    )
    firstname = models.CharField(
        'First name',
        max_length=255,
        default=None
    )

    othernames = models.CharField(
        'Other names',
        null=True,
        max_length=100,
        blank=True
    )

    email = models.EmailField(
        'Email',
        max_length=100,
        unique=True
    )

    company = models.ForeignKey(
        Company,
        null=False,
        blank=False,
        default=None,
        related_name='user_company',
        on_delete=models.PROTECT
    )

    auth_provider = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        default='email')

    date_joined = models.DateTimeField(
        'date joined',
        auto_now_add=True
    )

    last_login = models.DateTimeField(
        'last joined',
        auto_now=True
    )

    is_admin = models.BooleanField(
        default=False
    )

    is_verified = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=False
    )

    is_staff = models.BooleanField(
        default=False
    )

    is_superuser = models.BooleanField(
        default=False
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'othernames', 'company']

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }


@receiver(post_save, sender=User)
def email_new_account_credentials_handler(sender, instance, **kwargs):

    ctx = {
        "subject": "Account Created",
        "body": "client_account_created.html",
        "recipients": instance.email,
        "organization_url": instance.company,
        "email": instance.email,
        "password": instance.password,
        "full_name": f"{instance.firstname} {instance.othernames}",
        "template_name": "client_account_created.html"
    }

    Services.send_email_with_embeded_images(ctx)
