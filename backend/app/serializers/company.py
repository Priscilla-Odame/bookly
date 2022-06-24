from app.models.company import Company
from app.models.company_address import Address
from app.models.azure import AzureDetails
from rest_framework import serializers


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["id", "country", "city", "region", "street", "postal_code", ]
        read_only_fields = ('id',)

class AzureDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AzureDetails
        fields = ["id", "azure_account_name", "azure_account_key", ]
        read_only_fields = ('id',)


class CompanySerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    azure_details = AzureDetailsSerializer()

    def create(self, validated_data):
        address = validated_data.pop('address')
        new_address = Address.objects.create(**address,)
        azure_details = validated_data.pop('azure_details')
        new_azure_details = AzureDetails.objects.create(**azure_details,)
        new_company = Company.objects.create(
            **validated_data, address=new_address, azure_details=new_azure_details)

        return new_company

    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'address','azure_details')
        read_only_fields = ('id', 'created_by', 'published_at', 'deleted_at')
        depth = 1


class CompanyNamesSerializer(serializers.Serializer):

    def validate(self, attrs):

        companies = Company.objects.values("name").all()
        result = []
        for n in companies:
            result.append(n['name'])

        print(result)

        return {"names": result}
