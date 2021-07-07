from app.serializers.borrow import BorrowBookSerializer
from app.submodels.borrow import BorrowBook
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import viewsets, generics
from django.shortcuts import render


class BorrowBookViewSet(viewsets.ModelViewSet):
    serializer_class = BorrowBookSerializer
    queryset = BorrowBook.objects.all()
    filterset_fields = ['borrowed_by']

def borrow(request):
    return render(request,'borrow.html')

def dashboard(request):
    return render(request,'dashboard.html')

def admindashboard(request):
    return render(request,'admin.html')

class CountBorrowAPI(generics.ListAPIView):
    permission_classes = (IsAdminUser, IsAuthenticated)
    serializer_class = BorrowBookSerializer
    queryset = BorrowBook.objects.all()
    filterset_fields = ['borrowed_by',]

    def get(self,request,format = None):
        borrow = BorrowBook.objects.all()
        count = borrow.__len__()
        serializer = BorrowBookSerializer(borrow,many = True)
        return Response({"count":count, "data":serializer.data})
    