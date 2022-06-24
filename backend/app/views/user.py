from app.models.user import User
from app.models.company import Company
from rest_framework.response import Response
from app.serializers.user import RegisterSerializer, LoginSerializer, ValidateEmailSerializer, \
    ActivateDeactivateUserAccount, ListAllCompanyMembersSerializer
from rest_framework import generics, status, permissions, mixins
from django.contrib.sites.shortcuts import get_current_site
from app.utils import Utils
from asgiref.sync import sync_to_async
import asyncio
from django.utils.decorators import classonlymethod
from django.http.response import HttpResponse
from app.views.async_views import AsyncMixin, AsyncCreateModelMixin, AsyncDestroyModelMixin


class RegisterAPI(AsyncMixin, generics.CreateAPIView, AsyncCreateModelMixin, mixins.CreateModelMixin):
    """
    This is a public endpoint is used to register accounts for new users

    Sample Response:
{
        "firstname": "kwabena",
        "othernames": "asare",
        "email": "kwabena.asare@gmail.com",
        "company": 1
    }
    """
    permission_classes = [permissions.AllowAny, ]
    serializer_class = RegisterSerializer

    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view

    async def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)

        await sync_to_async(serializer.is_valid)(raise_exception=True)
        # serializer.is_valid(raise_exception=True)
        domain = get_current_site(self.request).domain
        email = serializer.validated_data.get('email', '')
        new_user = await sync_to_async(User.objects.get)(email=email)

        headers = self.get_success_headers(serializer.data)
        asyncio.create_task(
            Utils.send_email_verification_mail(new_user, domain))

        return Response(serializer.data, status.HTTP_201_CREATED, headers=headers)


class LoginAPI(generics.CreateAPIView):
    """
    This endpoint is used to log users in after registration

    Sample Response:
    {
    "id": 1,
    "firstname": "George",
    "othernames": "Awesome",
    "email": "george@somewhere.com",
    "company": 1,
    "tokens": {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyMzg1NTYwOSwianRpIjoiN2MzM2EzOGQzNTdjNDIwMmIzMjU2ZTY0MDMwZTgyOGEiLCJ1c2VyX2lkIjoxfQ.yiKiidzPPy9Z7xJd2wLtWlPMNcucefVBqoHpjMXaJUw",
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIzODU1NjA5LCJqdGkiOiIxYWMyNTYzNmIzYWE0MmYwOGI1OTI5YmUyZGZhMzJiZCIsInVzZXJfaWQiOjF9.NSMEVdmfw7JMb4yjaKFh_NBQXEl2P5SQ64hyCzBse-Q"
    }
}
    """
    permission_classes = [permissions.AllowAny, ]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)


class VerifyEmail(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = ActivateDeactivateUserAccount

    def get(self, request, uidb64, token):
        serializer = self.serializer_class()
        return Response(serializer.validate({"uidb64": uidb64, "token": token}))


class ValidateEmailView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = ValidateEmailSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response({'message': 'Email is valid and available',
                         'status_code': 200})


class ListAllCompanyMembersAPI(generics.GenericAPIView):
    """A class to enable the retrieving of all members of a company"""
    serializer_class = ListAllCompanyMembersSerializer
    queryset = User.objects

    def get(self, request):
        serializer = self.serializer_class()
        results = serializer.get_company_staff(
            {'company_id': self.request.user.company.id})

        return Response(results)
