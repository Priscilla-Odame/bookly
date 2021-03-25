from django.contrib import admin
from .models import User
from .books import Book
from .category import Category

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','firstname', 'lastname','email','password','date_of_birth')

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'date_of_publication', 'number_of_pages')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'books')


admin.site.register(User, UserAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)