# Generated by Django 3.1.2 on 2021-07-01 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_companyfileupload_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyfileupload',
            name='title',
        ),
    ]