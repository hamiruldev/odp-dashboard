# Generated by Django 4.0.3 on 2023-12-28 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='no_ic',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
