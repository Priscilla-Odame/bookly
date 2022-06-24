from rest_framework import serializers
from fruits.models import Fruit

class FruitSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    in_season = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Fruit(id=None, **validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance