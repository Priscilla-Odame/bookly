from django.contrib import admin
from app.models.user import User
from app.models.books import Book
from app.models.purchase import PurchaseBook

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','firstname', 'lastname','email','password','date_of_birth')

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','book_cover', 'author', 'date_of_publication', 'number_of_pages')

class PurchaseBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'purchased_by','date_purchased')

admin.site.register(User, UserAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(PurchaseBook, PurchaseBookAdmin)
