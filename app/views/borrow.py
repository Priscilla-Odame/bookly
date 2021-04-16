from app.serializers.borrow import OrderBookSerializer
from app.submodels.borrow import OrderBook
from rest_framework import viewsets
from django.shortcuts import render


class OrderBookViewSet(viewsets.ModelViewSet):
    serializer_class = OrderBookSerializer
    queryset = OrderBook.objects.all()

def borrow(request):
    return render(request,'borrow.html')
    
def dashboard(request):
    return render(request,'dashboard.html')

    