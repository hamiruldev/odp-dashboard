# Generated by Django 4.0.3 on 2023-12-28 21:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_newuser_no_ic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newuser',
            old_name='no_ic',
            new_name='ic_no',
        ),
        migrations.AddField(
            model_name='newuser',
            name='birth_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='newuser',
            name='ic_type',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
