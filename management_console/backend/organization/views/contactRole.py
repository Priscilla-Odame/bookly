from rest_framework.response import Response
from organization.serializers import  ContactRoleSerializer
from organization.models import ContactRole
from rest_framework import viewsets

class ContactRoleViewSet(viewsets.ModelViewSet):
    serializer_class = ContactRoleSerializer
    queryset = ContactRole.objects.all()