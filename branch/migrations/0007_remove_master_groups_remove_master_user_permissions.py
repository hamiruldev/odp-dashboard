# Generated by Django 4.0.3 on 2023-11-16 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0006_alter_master_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='master',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='master',
            name='user_permissions',
        ),
    ]
