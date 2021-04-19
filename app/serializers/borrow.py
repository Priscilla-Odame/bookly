from rest_framework import serializers
from app.submodels.borrow import OrderBook


class OrderBookSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['book'] = '%s' %(instance.book.title)
        ret['borrowed_by'] = '%s %s' %(instance.borrowed_by.firstname, instance.borrowed_by.lastname)
        return ret

    def create(self, validated_data):
        validated_data['borrowed_by'] = self.context['request'].user
        return super().create(validated_data)
    class Meta:
        model = OrderBook
        fields = '__all__'
        read_only_fields = ('date_borrowed','borrowed_by','return_date')