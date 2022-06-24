from rest_framework.response import Response
from organization.serializers import AdministratorSerializer
from organization.models import Administrator
from rest_framework import viewsets

class AdministratorViewSet(viewsets.ModelViewSet):
    serializer_class = AdministratorSerializer
    queryset = Administrator.objects.all()
    filterset_fields = ('organization',)
