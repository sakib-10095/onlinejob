# Generated by Django 5.0.6 on 2024-06-08 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_rename_job_aplly_model_job_apply_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_apply_model',
            name='apply_resume',
            field=models.FileField(null=True, upload_to='media/apply_resume'),
        ),
    ]
