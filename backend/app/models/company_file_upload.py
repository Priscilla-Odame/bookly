import os
from django.db import models
from app.file_validator import validate_file
from app.models.user import User
from app.models.company import Company

from django.db.models.signals import post_save
from django.dispatch import receiver
from app.utils import Utils
from app.models.Soft_deletion import SoftDeletionModel
from asgiref.sync import sync_to_async
import asyncio
from azure.storage.blob import BlockBlobService
from storages.backends.azure_storage import AzureStorage
import shutil


class CompanyFileUpload(SoftDeletionModel):

    name = models.CharField(
        max_length=100,
        null=True,
        unique=False,
        blank=True,
        default="file name"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='company_file_uploads'
    )

    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    data_file = models.FileField(
        upload_to=Utils.create_company_file_upload_path,
        blank=True,
        null=True,
        validators=[validate_file]
    )

    comment = models.CharField(
        max_length=400,
        null=True,
        unique=False
    )

    file_size = models.CharField(
        max_length=100,
        null=True,
        unique=False,
        blank=True,
        default="null"
    )

    def save(self, *args, **kwargs):
        size = self.data_file.size
        power = 2**10
        n = 0
        power_labels = {0: '', 1: 'Kilo', 2: 'Mega', 3: 'Giga', 4: 'Tera'}
        while size > power:
            size /= power
            n += 1

        self.file_size = f"{size:.2f} {power_labels[n]}bytes"
        self.name = self.data_file.name

        super(CompanyFileUpload, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.data_file}, {self.user}'


@receiver(post_save, sender=CompanyFileUpload)
async def email_report_details_handler(sender, instance, **kwargs):

    ctx = {
        "firstname": instance.user.firstname,
        "timestamp": instance.timestamp,
        "fullname_and_email": f"{instance.user.firstname} {instance.user.othernames}",
        "subject": "File Upload",
        "recepient": instance.user.email,
        "email": instance.user.email,
        "url": instance.data_file.url,
        "comment": instance.comment
    }
    asyncio.create_task(Utils.send_report_email(ctx))

@receiver(post_save, sender=CompanyFileUpload)
def delete_handler(sender, instance, **kwargs):
    # shutil.rmtree('backend/{instance.user.company}', ignore_errors=True)
    # print(f'-------------{instance.user.company}')
    block_blob_service = BlockBlobService(account_name='pistorage01', account_key=os.environ.get("AZURE_ACCOUNT_KEY"))
    container_name = 'media'
    block_blob_service.delete_blob(container_name,instance.data_file)