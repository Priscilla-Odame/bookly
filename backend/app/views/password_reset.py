from rest_framework import generics, status, permissions, mixins
from app.serializers.password_reset import PasswordResetEmailRequestSerializer, SetNewPasswordSerializer
from rest_framework.response import Response
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from app.models.user import User
from django.contrib.sites.shortcuts import get_current_site
from app.views.async_views import AsyncMixin, AsyncCreateModelMixin, AsyncDestroyModelMixin
from asgiref.sync import sync_to_async, async_to_sync
import asyncio
from app.utils import Utils
from django.core.exceptions import ValidationError
from django.utils.decorators import classonlymethod


class RequestPasswordEmailReset(AsyncMixin, generics.GenericAPIView, AsyncCreateModelMixin, mixins.CreateModelMixin):
    permission_classes = (permissions.AllowAny,)

    serializer_class = PasswordResetEmailRequestSerializer

    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view

    async def post(self, request):

        serializer = self.serializer_class(data=request.data)

        await sync_to_async(serializer.is_valid)(raise_exception=True)

        email = self.request.user.email
        current_user = await sync_to_async(User.objects.filter)(email=email)

        if current_user.exists():

            if self.request.META.get('HTTP_ORIGIN', None):
                current_site = self.request.META.get('HTTP_ORIGIN')
                asyncio.create_task(
                    Utils.send_password_reset_email(email, current_site))

            else:
                raise ValidationError("Can not obtain user request domain")
        else:
            raise ValidationError("The provided email does not exit. ")

        headers = self.get_success_headers(serializer.data)

        # serializer.is_valid(raise_exception=True)

        return Response({'success': "A link to reset your password has just been sent to your email"},
                        status=status.HTTP_200_OK, headers=headers)


class PasswordTokenCheckAPI(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, uidb64, token):

        try:
            user_pk = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=user_pk)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({"error": "Invalid token, please request a new one"},
                                status=status.HTTP_401_UNAUTHORIZED)

            return Response({"success": True,
                             "message": "Credentials Valid",
                             "uidb64": uidb64,
                             "token": token},
                            status=status.HTTP_200_OK)

        except DjangoUnicodeDecodeError as identifier:

            return Response({"error": "Invalid token, please request a new one"},
                            status=status.HTTP_401_UNAUTHORIZED)


class SetNewPasswordAPI(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)

    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response({"success": True,
                         "message": "Password reset successful"},
                        status=status.HTTP_200_OK)
