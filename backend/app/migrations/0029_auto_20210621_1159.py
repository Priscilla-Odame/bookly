# Generated by Django 3.1.2 on 2021-06-21 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_user_auth_provider'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyfileupload',
            name='file_size',
            field=models.CharField(blank=True, default='null', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fileupload',
            name='file_size',
            field=models.CharField(default='null', max_length=100, null=True),
        ),
    ]