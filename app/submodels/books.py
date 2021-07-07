from django.db import models
from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.files.base import ContentFile
from django.core.files.uploadhandler import UploadFileException

class Book(models.Model):
    title = models.CharField(max_length=100)
    book_cover = models.ImageField(upload_to = 'images', blank = True,null=True)
    author = models.CharField(max_length=100)
    date_of_publication = models.DateField(default=date.today)
    number_of_pages = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5000)])
    copies = models.IntegerField(default = 0, validators=[MinValueValidator(0), MaxValueValidator(2000)])
    max_borrow_duration = models.PositiveIntegerField( validators=[MinValueValidator(3), MaxValueValidator(20)], default = 3)

    
    class Meta:
        unique_together = [['title', 'author']]

    def __str__(self) -> str:
        return self.title
