# Generated by Django 4.0.3 on 2023-12-28 21:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_no_ic_newuser_ic_no_newuser_birth_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='birth_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
