from django.contrib import admin
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','firstname', 'lastname','email','password','username','date_of_birth')


admin.site.register(User, UserAdmin)