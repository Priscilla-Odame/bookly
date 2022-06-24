from rest_framework.response import Response
from organization.serializers import OrganizationStatusSerializer
from organization.models import OrganizationStatus
from rest_framework import viewsets

class OrganizationStatusViewSet(viewsets.ModelViewSet):
    serializer_class = OrganizationStatusSerializer
    queryset = OrganizationStatus.objects.all()