# Generated by Django 5.0.6 on 2024-05-29 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_jobseekerprofile_recruiterprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='addjob_model',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='media/profile_picture'),
        ),
    ]
