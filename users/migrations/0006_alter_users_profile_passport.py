# Generated by Django 4.0.4 on 2022-08-05 10:32

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_users_profile_ecology_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users_profile',
            name='passport',
            field=models.FileField(upload_to=users.models.user_directory_passport),
        ),
    ]