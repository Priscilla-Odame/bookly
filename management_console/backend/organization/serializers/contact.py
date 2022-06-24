from rest_framework import serializers
from organization.models import Contact, Organization

class ContactSerializer(serializers.ModelSerializer):
    organization = serializers.HyperlinkedRelatedField(
        view_name = 'organizations-detail',
        queryset = Organization.objects.all()
    )

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['name'] = f'{instance.staff_member.firstname} {instance.staff_member.lastname}'
        ret['role'] = f'{instance.role.name}'
        ret['status'] = f'{instance.status.name}' 
        ret['updated_by'] = f'{instance.updated_by.firstname} {instance.updated_by.lastname}'
        return ret

    def create(self, validated_data):
        validated_data['updated_by'] = self.context['request'].user
        return super().create(validated_data)
    class Meta:
        model = Contact
        fields = "__all__"
        read_only_fields = ['updated_by']

        # depth = 1