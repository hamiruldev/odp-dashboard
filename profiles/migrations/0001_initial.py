# Generated by Django 4.0.3 on 2023-12-17 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import profiles.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50, null=True)),
                ('photo', models.ImageField(default='profile_photo/avatar.png', upload_to=profiles.models.get_upload_path)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('email', models.CharField(max_length=100)),
                ('nickname', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('youtube', models.URLField(blank=True, null=True)),
                ('tiktok', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('top_seller', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_hired', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('view_count', models.IntegerField(blank=True, default=0)),
            ],
        ),
    ]
