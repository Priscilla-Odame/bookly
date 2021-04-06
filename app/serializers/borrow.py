from rest_framework import serializers
from app.submodels.borrow import OrderBook


class OrderBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderBook
        fields = '__all__'