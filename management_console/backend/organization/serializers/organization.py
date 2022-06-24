from rest_framework import serializers
from organization.models import Organization

class OrganizationSerializer(serializers.ModelSerializer):
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['status'] = '%s' %(instance.status.name)
        ret['updated_by'] = '%s %s' %(instance.updated_by.firstname, instance.updated_by.lastname)
        return ret

    def create(self, validated_data):
        validated_data['updated_by'] = self.context['request'].user
        return super().create(validated_data)
    class Meta:
        model = Organization
        fields = "__all__"
        read_only_fields = ['updated_by']