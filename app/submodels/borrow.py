from django.db import models
from app.models import User
from .books import Book
from datetime import date
from django.utils import timezone
from datetime import datetime, timedelta
from django.core.validators import MinValueValidator, MaxValueValidator


class BorrowBook(models.Model):

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_by = models.ForeignKey(User, related_name='borrower', on_delete=models.CASCADE)
    date_borrowed = models.DateTimeField(default=timezone.now, null= False, blank = False)
    duration = models.IntegerField(validators=[MinValueValidator(3), MaxValueValidator(20)], default = 3)
    return_date = models.DateTimeField(default=datetime.today() + timedelta(days=3))

    class Meta:
        unique_together = [['book', 'borrowed_by']]


    # def get_deadline(self):
    #     borrow_date = datetime.strptime(date_borrowed, "FORMAT")
    #     return_date = borrow_date + timedelta(days=duration)
    #     return_by = return_date.strftime(return_date, days)

    # def get_deadline(self):
    #     attname = 'duration'.format() # get the attribute name
    #     value = getattr(self, attname) # get the value
    #     return_date = borrow_date + timedelta(days=value)
    #     return str(return_date)
    # user_deadline = property(get_deadline)
