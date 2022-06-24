from rest_framework.response import Response
from organization.serializers import  ContactStatusSerializer
from organization.models import ContactStatus
from rest_framework import viewsets

class ContactStatusViewSet(viewsets.ModelViewSet):
    serializer_class = ContactStatusSerializer
    queryset = ContactStatus.objects.all()