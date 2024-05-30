# Generated by Django 5.0.6 on 2024-05-28 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='addjob_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobTitle', models.CharField(max_length=100, null=True)),
                ('companyName', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(max_length=100, null=True)),
                ('location', models.CharField(max_length=100, null=True)),
                ('creat_time', models.TimeField(auto_now_add=True, null=True)),
                ('update_time', models.TimeField(auto_now=True, null=True)),
            ],
        ),
    ]
