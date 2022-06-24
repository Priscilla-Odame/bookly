from app.serializers.oauth import OAuthSerializer, CompanyWhitelistSerializer
from rest_framework.response import Response
from rest_framework import generics, status, permissions
from app.utils import Utils
from django.contrib.sites.shortcuts import get_current_site
from app.models.user import User


class OAuthAPI(generics.CreateAPIView):
    """
    This endpoint is used to log users into the platform using third party accounts

    Sample Response:
{
    "id": 2,
    "firstname": "Peter",
    "othernames": "Nortey",
    "email": "Peter.Nortey@azubiafrica.org",
    "company": 1,
    "tokens": {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyNDM2Mzg5NiwianRpIjoiM2YwYTAwOTJlZmUyNDJjY2FmNTg0Y2YyZmI2NmJiMTUiLCJ1c2VyX2lkIjoyfQ.dHIrwS8j09ePLEYdvXj-2q_dMOOfFwzXi8D3m_Ou4vk",
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI0MzYzODk2LCJqdGkiOiIxOGRmNzMxOWZlMzU0NzEwYjU4ODlkMmViMzBjNWQ1MCIsInVzZXJfaWQiOjJ9.Bd_xqqneay3GfrvVXvScjlPQtTnPmFi7Mms0ETjFDVg"
    }
}
    """
    permission_classes = [permissions.AllowAny, ]
    serializer_class = OAuthSerializer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)

class CompanyWhitelistAPI(generics.CreateAPIView):

    """
    This endpoint is used to log users into the platform using third party accounts

    Sample Response:
   {
            "name":"Nestle Whitelist",
            "domain_names":["azubi.org"],
            "company":2
    }
    """

    permission_classes = [permissions.AllowAny, ]
    serializer_class = CompanyWhitelistSerializer

