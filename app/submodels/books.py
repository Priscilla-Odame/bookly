from django.db import models
from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator

class Book(models.Model):
    title = models.CharField(max_length=100)
    book_cover = models.ImageField(upload_to = '', blank = True,null=True)
    author = models.CharField(max_length=100)
    date_of_publication = models.DateField(default=date.today)
    number_of_pages = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5000)])
    number_of_books = models.IntegerField(default = 0, validators=[MinValueValidator(0), MaxValueValidator(2000)])
    max_borrow_duration = models.PositiveIntegerField( validators=[MinValueValidator(3), MaxValueValidator(20)], default = 3)

    def __str__(self) -> str:
        return self.title
