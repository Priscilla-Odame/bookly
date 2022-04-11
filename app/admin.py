from django.contrib import admin
from app.models.user import User
# from app.submodels.books import Book
# from app.submodels.category import Category
# from app.submodels.purchase import OrderBook

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','firstname', 'lastname','email','password','date_of_birth')
