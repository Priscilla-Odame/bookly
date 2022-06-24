from rest_framework.response import Response
from organization.serializers import  AdministratorStatusSerializer
from organization.models import  AdministratorStatus
from rest_framework import viewsets

class  AdministratorStatusViewSet(viewsets.ModelViewSet):
    serializer_class = AdministratorStatusSerializer
    queryset = AdministratorStatus.objects.all()