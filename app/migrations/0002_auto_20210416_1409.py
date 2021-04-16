# Generated by Django 3.1.6 on 2021-04-16 14:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='max_borrow_duration',
            field=models.PositiveIntegerField(default=3, validators=[django.core.validators.MinValueValidator(3), django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='book',
            name='number_of_books',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2000)]),
        ),
        migrations.AlterField(
            model_name='book',
            name='number_of_pages',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5000)]),
        ),
    ]
