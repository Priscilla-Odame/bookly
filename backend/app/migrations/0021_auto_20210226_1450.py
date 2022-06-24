# Generated by Django 3.1.2 on 2021-02-26 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20210226_1450'),
        ('projectapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='data_file', to='projectapp.project'),
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='ProjectDashboard',
        ),
        migrations.DeleteModel(
            name='ProjectMember',
        ),
        migrations.DeleteModel(
            name='ProjectMemberRole',
        ),
    ]