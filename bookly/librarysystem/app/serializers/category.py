from rest_framework import serializers
from app.category import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'