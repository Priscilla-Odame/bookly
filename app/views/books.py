from django.shortcuts import render
from app.submodels.books import Book
from app.serializers.books import BookSerializer
from rest_framework import viewsets, generics
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.http import HttpResponse


class BookViews(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filterset_fields = ['title', 'author']

def books(request):
    # all_books = Book.objects.all()
    # filterset_fields = ['title','author']
    # args = {'all_books': all_books}
    return render(request,'books.html')

class CountAPI(generics.GenericAPIView):
    permission_classes = (IsAdminUser, IsAuthenticated)
    serializer_class = BookSerializer

    def get(self,request,format = None):
        book = Book.objects.all()
        count = book.__len__()
        serializer = BookSerializer(book,many = True)
        return Response({"count":count, "data":serializer.data})