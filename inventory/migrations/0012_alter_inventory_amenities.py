# Generated by Django 4.0.3 on 2024-01-14 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_alter_inventory_lat_alter_inventory_long'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='amenities',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]