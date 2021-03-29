from app.submodels.books import Book
from app.serializers.books import BooksSerializer
from rest_framework import viewsets


class BookViews(viewsets.ModelViewSet):
    serializer_class = BooksSerializer
    queryset = Book.objects.all()
    filterset_fields = ['title', 'author']