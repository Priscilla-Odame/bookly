from django.contrib import admin
from .models import User
from app.submodels.books import Book
from app.submodels.category import Category
from app.submodels.borrow import OrderBook

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','firstname', 'lastname','email','password','date_of_birth')

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','book_cover', 'author', 'date_of_publication', 'number_of_pages','number_of_books','max_borrow_duration')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'books')

class OrderBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'borrowed_by','date_borrowed','return_date')

admin.site.register(User, UserAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(OrderBook, OrderBookAdmin)