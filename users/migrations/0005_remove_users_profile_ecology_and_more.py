# Generated by Django 4.0.4 on 2022-08-05 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_users_profile_ecology_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users_profile',
            name='ecology',
        ),
        migrations.RemoveField(
            model_name='users_profile',
            name='med_spravka',
        ),
        migrations.RemoveField(
            model_name='users_profile',
            name='strakhovka',
        ),
        migrations.RemoveField(
            model_name='users_profile',
            name='talon',
        ),
        migrations.RemoveField(
            model_name='users_profile',
            name='tax',
        ),
        migrations.RemoveField(
            model_name='users_profile',
            name='tech_osmotr',
        ),
        migrations.RemoveField(
            model_name='users_profile',
            name='tech_passport',
        ),
        migrations.RemoveField(
            model_name='users_profile',
            name='tonirovka',
        ),
        migrations.RemoveField(
            model_name='users_profile',
            name='udost_von_gas_balon_auto',
        ),
        migrations.AlterField(
            model_name='users_profile',
            name='passport',
            field=models.FileField(upload_to='passports/<function user_directory_path at 0x00000196DA8B5D30>'),
        ),
    ]
