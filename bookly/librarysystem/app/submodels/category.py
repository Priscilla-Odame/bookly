from django.db import models
from .books import Book

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    books = models.ForeignKey('Book', related_name='books', on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name

