from django.db import models
from datetime import date

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date_of_publication = models.DateField(default=date.today)
    number_of_pages = models.IntegerField()

    def __str__(self) -> str:
        return self.title
