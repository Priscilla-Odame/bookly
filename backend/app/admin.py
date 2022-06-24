from django.contrib import admin
from .models import User, FileUpload, Company
from app.models.company_address import Address
from app.models.azure import AzureDetails
from .admin_soft_deletion import SoftDeletionAdmin
from django.contrib.contenttypes.models import ContentType
from django.utils.html import format_html
from django.urls import reverse
from app.models.oauth_whitelist import CompaniesWhitelist
from app.models.company_file_upload import CompanyFileUpload


def linkify(field_name):
    """
    Converts a foreign key value into clickable links.

    If field_name is 'parent', link text will be str(obj.parent)
    Link will be admin url for the admin url for obj.parent.id:change
    """

    def _linkify(obj):
        content_type = ContentType.objects.get_for_model(obj)
        app_label = content_type.app_label
        linked_obj = getattr(obj, field_name)
        linked_content_type = ContentType.objects.get_for_model(linked_obj)
        model_name = linked_content_type.model
        view_name = f"admin:{app_label}_{model_name}_change"
        link_url = reverse(view_name, args=[linked_obj.pk])
        return format_html('<a href="{}">{}</a>', link_url, linked_obj)

    _linkify.short_description = field_name.replace("_", " ").capitalize()
    return _linkify


class UserAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'firstname',
                    'othernames',
                    'email'
                    )


class FileUploadAdmin(SoftDeletionAdmin):
    list_display = ("id",
                    "project",
                    "user",
                    "title",
                    "timestamp",
                    "data_file",
                    "deleted_at"
                    )


class CompanyFileUploadAdmin(SoftDeletionAdmin):
    list_display = ("id",
                    "user",
                    "timestamp",
                    "data_file",
                    "comment",
                    "deleted_at",
                    )


class AddressAdmin(SoftDeletionAdmin):
    list_display = ('id',
                    'street',
                    'city',
                    'region',
                    'country',
                    'postal_code'
                    )

class AzureDetailsAdmin(SoftDeletionAdmin):
    list_display = ('id',
                    'azure_account_name',
                    'azure_account_key',
                    )


class CompanyAdmin(SoftDeletionAdmin):
    list_display = ('id',
                    'name',
                    'description',
                    'published_at',
                    'deleted_at',
                    linkify(field_name='address'),
                    linkify(field_name='azure_details')
                    )


class WhitelistedDomainsAdmin(SoftDeletionAdmin):
    list_display = ("id",
                    "name",
                    "domain_names",
                    "company"
                    )


admin.site.register(User, UserAdmin)
admin.site.register(FileUpload, FileUploadAdmin)
admin.site.register(CompanyFileUpload, CompanyFileUploadAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(CompaniesWhitelist, WhitelistedDomainsAdmin)
admin.site.register(AzureDetails, AzureDetailsAdmin)
