from organization.models.profile import Profile
from organization.serializers.profile import ProfileSerializer
from rest_framework import viewsets


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()