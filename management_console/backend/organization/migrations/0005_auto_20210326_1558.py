# Generated by Django 3.1.2 on 2021-03-26 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_auto_20210326_1532'),
    ]

    operations = [
        migrations.RenameField(
            model_name='administrator',
            old_name='profile_pic',
            new_name='profile',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='profile_pic',
            new_name='profile',
        ),
    ]
