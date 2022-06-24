from django.db import models
from app.file_validator import validate_file
from app.models.user import User
from app.models.company import Company

from django.db.models.signals import post_save
from django.dispatch import receiver
from app.utils import Utils
from app.models.Soft_deletion import SoftDeletionModel


class CompanyDirectoryFilesUpload(SoftDeletionModel):

    name = models.CharField(
        max_length=100,
        null=True,
        unique=False,
        blank=True,
        default="directory_file_name"
    )

    directory = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        unique=False
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='company_drectory_upload'
    )

    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    data_file = models.FileField(
        upload_to=Utils.create_directory_path,
        blank=True,
        null=True,
        validators=[validate_file]
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

        super(CompanyDirectoryFilesUpload, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.data_file}, {self.user}'

# @receiver(post_save, sender=CompanyFileUpload)
# def email_report_details_handler(sender, instance, **kwargs):

#     ctx = {
#         "firstname": instance.user.firstname,
#         "timestamp": instance.timestamp,
#         "fullname_and_email": f"{instance.user.firstname} {instance.user.othernames}",
#         "subject": "Directory Upload",
#         "recepient": instance.user.email,
#         "email": instance.user.email,
#         "url": instance.data_file.url,
#         "comment": instance.comment
#     }

#     Utils.send_report_email(ctx)
