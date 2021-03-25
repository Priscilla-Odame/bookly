from rest_framework import serializers
from app.books import Book


class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        feilds = '__all__'