# Generated by Django 4.0.4 on 2022-08-10 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_users_profile_passport'),
    ]

    operations = [
        migrations.AddField(
            model_name='users_profile',
            name='ecology',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='users_profile',
            name='med_spravka',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='users_profile',
            name='strakhovka',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='users_profile',
            name='talon',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='users_profile',
            name='tax',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='users_profile',
            name='tech_osmotr',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='users_profile',
            name='tech_passport',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='users_profile',
            name='tonirovka',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='users_profile',
            name='udost_von_gas_balon_auto',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='users_profile',
            name='passport',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='users_profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]