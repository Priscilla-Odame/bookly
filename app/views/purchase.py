from app.serializers.purchase import PurchaseBookSerializer
from app.models.purchase import PurchaseBook
from rest_framework import viewsets


class PurchaseBookViewSet(viewsets.ModelViewSet):
    serializer_class = PurchaseBookSerializer
    queryset = PurchaseBook.objects.all()
    