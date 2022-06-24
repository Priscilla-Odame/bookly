from rest_framework import serializers
from auths.models import User


class RetrieveAllStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','firstname','lastname','email','phone_number','is_staff')