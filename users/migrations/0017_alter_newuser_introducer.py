# Generated by Django 4.0.3 on 2024-01-14 02:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_newuser_listing_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='introducer',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
