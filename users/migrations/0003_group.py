# Generated by Django 4.0.3 on 2023-11-06 12:08

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_newuser_groupid_newuser_introducer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logoUrl', models.ImageField(blank=True, null=True, upload_to=users.models.get_upload_path, verbose_name='LogoUrl')),
                ('empires', models.PositiveIntegerField()),
                ('branch', models.CharField(max_length=100)),
                ('founder', models.CharField(max_length=100)),
            ],
        ),
    ]