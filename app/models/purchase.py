from django.db import models
from app.models.user import User
from .books import Book
from datetime import date
from django.utils import timezone


class PurchaseBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    purchased_by = models.ForeignKey(User, related_name='purchaser', on_delete=models.CASCADE)
    date_purchased = models.DateTimeField(default=timezone.now)
