from rest_framework.response import Response
from organization.serializers import ContactSerializer
from organization.models import Contact
from rest_framework import viewsets

class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    filterset_fields = ('organization',)