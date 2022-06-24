from rest_framework import serializers
from django.core.mail import EmailMessage
from rest_framework.exceptions import AuthenticationFailed

from app.models.user import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, force_bytes, DjangoUnicodeDecodeError, smart_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.template.loader import get_template
import os
from smtplib import SMTPException
from app.utils import Utils
from django.core.exceptions import ValidationError


class PasswordResetEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2, required=True)

    class Meta:
        fields = ('email',)


class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        min_length=6, max_length=67,
        write_only=True
    )
    token = serializers.CharField(
        min_length=1,
        write_only=True
    )
    uidb64 = serializers.CharField(
        min_length=2,
        write_only=True
    )

    class Meta:
        fields = ['password', 'token', 'uidb64']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed(
                    'The reset token or id is invalid', 401)

            user.set_password(password)
            user.save()

            return user

        except Exception as e:
            raise AuthenticationFailed('The reset token or id is invalid', 401)

        return super().validate(attrs)
