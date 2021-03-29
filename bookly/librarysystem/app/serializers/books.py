from rest_framework import serializers
from app.submodels.books import Book


class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'