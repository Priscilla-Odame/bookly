from rest_framework.response import Response
from organization.serializers import OrganizationSerializer
from organization.models import Organization
from rest_framework import viewsets

class OrganizationViewSet(viewsets.ModelViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()