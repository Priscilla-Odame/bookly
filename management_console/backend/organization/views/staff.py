from rest_framework import viewsets
from auths.models import User
from organization.serializers.staff import RetrieveAllStaffSerializer

class RetrieveAllStaffViewSet(viewsets.ModelViewSet):
    serializer_class = RetrieveAllStaffSerializer
    queryset = User.objects.all()
    filterset_fields = ('is_staff',)
    http_method_names = ['get', 'head']