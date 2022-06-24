import os
from django.db import models
from app.file_validator import validate_file
from app.models.user import User
from projectapp.models.project import Project
from django.db.models.signals import post_save
from django.dispatch import receiver
from app.utils import Utils
from app.models.Soft_deletion import SoftDeletionModel
from asgiref.sync import sync_to_async
import asyncio


class FileUpload(SoftDeletionModel):

    project = models.ForeignKey(
        'projectapp.Project',
        on_delete=models.PROTECT,
        related_name='data_file'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='project_file_uploads'
    )
    title = models.CharField(
        max_length=100,
        null=False,
        unique=True
    )
    timestamp = models.DateTimeField(
        auto_now_add=True
    )
    data_file = models.FileField(
        upload_to=Utils.create_path,
        blank=True,
        null=True,
        validators=[validate_file]
    )

    file_size = models.CharField(
        max_length=100,
        null=True,
        unique=False,
        default="null"
    )

    def save(self, *args, **kwargs):
        '''
        since the file received by this function is a file object not a django inmemoryuploadedfile object
        we need to find another way of getting the file size
        '''
        # print(type(self.data_file))
        
        size = self.data_file.size
        power = 2**10
        n = 0
        power_labels = {0: '', 1: 'Kilo', 2: 'Mega', 3: 'Giga', 4: 'Tera'}
        while size > power:
            size /= power
            n += 1

        self.file_size = f"{size:.2f} {power_labels[n]}bytes"

        super(FileUpload, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}, {self.user}, {self.project}'


@receiver(post_save, sender=FileUpload)
async def email_report_details_handler(sender, instance, **kwargs):

    ctx = {
        "firstname": instance.user.firstname,
        "project_name": instance.project.name,
        "title": instance.title,
        "timestamp": instance.timestamp,
        "fullname_and_email": f"{instance.user.firstname} {instance.user.othernames}",
        "subject": "File Upload",
        "recepient": instance.user.email,
        "email": instance.user.email,
        "url": instance.data_file.url
    }
    asyncio.create_task(Utils.send_report_email(ctx))
