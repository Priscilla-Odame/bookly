# Generated by Django 3.1.2 on 2021-07-15 21:28

import app.file_validator
import app.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_companyfileupload_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyfileupload',
            name='data_file',
            field=models.FileField(blank=True, null=True, upload_to=app.utils.Utils.create_company_file_upload_path, validators=[app.file_validator.validate_file]),
        ),
        migrations.CreateModel(
            name='CompanyDirectoryFilesUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(blank=True, default='directory_file_name', max_length=100, null=True)),
                ('directory', models.CharField(blank=True, max_length=100, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('data_file', models.FileField(blank=True, null=True, upload_to=app.utils.Utils.create_directory_path, validators=[app.file_validator.validate_file])),
                ('file_size', models.CharField(blank=True, default='null', max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_drectory_upload', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
