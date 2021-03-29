from app.serializers.borrow import OrderBookSerializer
from app.submodels.borrow import OrderBook
from rest_framework import viewsets


class OrderBookViewSet(viewsets.ModelViewSet):
    serializer_class = OrderBookSerializer
    queryset = OrderBook.objects.all()
    