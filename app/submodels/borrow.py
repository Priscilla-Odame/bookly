from django.db import models
from app.models import User
from .books import Book
from datetime import date
from django.utils import timezone


class OrderBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_by = models.ForeignKey(User, related_name='borrower', on_delete=models.CASCADE)
    date_borrowed = models.DateTimeField(default=timezone.now, null= False, blank = False)
    return_date = models.DateTimeField(default=timezone.now)
