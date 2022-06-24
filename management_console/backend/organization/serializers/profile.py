from rest_framework import serializers
from organization.models.profile import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'