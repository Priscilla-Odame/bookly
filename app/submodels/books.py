from django.db import models
from datetime import date

class Book(models.Model):
    title = models.CharField(max_length=100)
    book_cover = models.ImageField(upload_to = 'uploads/', blank = True,null=True)
    author = models.CharField(max_length=100)
    date_of_publication = models.DateField(default=date.today)
    number_of_pages = models.IntegerField()
    number_of_books = models.IntegerField(default = 0)

    def __str__(self) -> str:
        return self.title
