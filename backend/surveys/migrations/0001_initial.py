# Generated by Django 3.1.2 on 2021-03-09 14:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projectapp', '0004_projectmember_approval_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('question_count', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('survey_deadline', models.DateTimeField(default=None)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='data_file', to='projectapp.project')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
