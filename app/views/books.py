from django.shortcuts import render
from app.submodels.books import Book
from app.serializers.books import BooksSerializer
from rest_framework import viewsets


class BookViews(viewsets.ModelViewSet):
    serializer_class = BooksSerializer
    queryset = Book.objects.all()
    filterset_fields = ['title', 'author']

def books(request):
    all_books = Book.objects.all()
    filterset_fields = ['title','author']
    args = {'all_books': all_books}
    return render(request,'books.html',args)