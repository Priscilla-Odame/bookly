from django.contrib import admin

from .models import OrganizationStatus, Organization, Contact, ContactStatus, ContactRole, Administrator, AdministratorStatus, Profile
# Register your models here.

class OrganizationStatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'updated_at')

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name','updated_by','updated_at')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('staff_member','role','status','updated_by','updated_at')

class ContactStatusAdmin(admin.ModelAdmin):
    list_display = ('name','updated_by','updated_at')

class ContactRoleAdmin(admin.ModelAdmin):
    list_display = ('name','updated_by','updated_at')

class AdministratorAdmin(admin.ModelAdmin):
    list_display = ('name','organization','status','updated_by','updated_at')

class AdministratorStatusAdmin(admin.ModelAdmin):
    list_display = ('name','updated_by','updated_at')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','profile_pic')

admin.site.register(OrganizationStatus, OrganizationStatusAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactStatus, ContactStatusAdmin)
admin.site.register(ContactRole, ContactRoleAdmin)
admin.site.register(Administrator, AdministratorAdmin)
admin.site.register(AdministratorStatus, AdministratorStatusAdmin)
admin.site.register(Profile, ProfileAdmin)