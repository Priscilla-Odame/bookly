from rest_framework import serializers
from app.models.books import Book


class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'