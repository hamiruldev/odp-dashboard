# Generated by Django 4.0.3 on 2024-01-04 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_profile_is_agent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='phone',
            new_name='phone_no',
        ),
    ]