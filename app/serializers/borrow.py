from rest_framework import serializers
from app.submodels.borrow import OrderBook


class OrderBookSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        validated_data['borrowed_by'] = self.context['request'].user
        return super().create(validated_data)
    class Meta:
        model = OrderBook
        fields = '__all__'
        read_only_fields = ('date_borrowed','borrowed_by')