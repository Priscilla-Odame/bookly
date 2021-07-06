from app.serializers.borrow import BorrowBookSerializer
from app.submodels.borrow import BorrowBook
from rest_framework import viewsets
from django.shortcuts import render


class BorrowBookViewSet(viewsets.ModelViewSet):
    serializer_class = BorrowBookSerializer
    queryset = BorrowBook.objects.all()

def borrow(request):
    return render(request,'borrow.html')

def dashboard(request):
    return render(request,'dashboard.html')

def admindashboard(request):
    return render(request,'admin.html')
    