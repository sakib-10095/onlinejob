# Generated by Django 5.0.6 on 2024-05-29 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_addjob_model_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addjob_model',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='media/profile_picture'),
        ),
    ]