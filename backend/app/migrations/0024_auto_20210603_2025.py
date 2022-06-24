# Generated by Django 3.1.2 on 2021-06-03 20:25

import app.file_validator
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20210603_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='data_file',
            field=models.FileField(blank=True, null=True, upload_to='File', validators=[app.file_validator.validate_file]),
        ),
    ]
