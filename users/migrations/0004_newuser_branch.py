# Generated by Django 4.0.3 on 2023-11-06 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='branch',
            field=models.CharField(max_length=200, null=True),
        ),
    ]