from rest_framework import serializers
from django.core.mail import EmailMessage
from rest_framework.exceptions import AuthenticationFailed

from app.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.template.loader import get_template
import os


class PasswordResetEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2, required=False)

    class Meta:
        fields = ('email',)

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.pk))
            token = PasswordResetTokenGenerator().make_token(user)
            request = self.context.get("request")
            current_site = get_current_site(request=request).domain
            link = reverse("password_reset_confirm",
                           kwargs={
                               "uidb64": uidb64,
                               "token": token
                           })
            reset_password_url = f"http://{current_site}{link}"
            ctx = {
                "firstname": user.firstname,
                "PasswordResetLink": reset_password_url,
            }
            message = get_template("password_reset_email.html").render(ctx)
            email = EmailMessage(
                "Password Reset",
                message,
                os.environ.get("EMAIL_HOST_USER"),
                [user.email],
            )
            email.content_subtype = "html"
            email.send()

        return super().validate(attrs)


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
                raise AuthenticationFailed('The reset link is invalid', 401)

            user.set_password(password)
            user.save()

            return user

        except Exception as e:
            raise AuthenticationFailed('The reset link is invalid', 401)

        return super().validate(attrs)
