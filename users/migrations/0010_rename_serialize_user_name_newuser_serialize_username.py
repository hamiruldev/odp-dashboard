# Generated by Django 4.2.7 on 2023-11-27 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_newuser_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newuser',
            old_name='serialize_user_name',
            new_name='serialize_username',
        ),
    ]
