# Generated by Django 3.1.2 on 2021-03-26 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0002_auto_20210325_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
