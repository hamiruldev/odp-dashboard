# Generated by Django 4.0.3 on 2023-11-26 06:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='blog.category'),
        ),
        migrations.AddField(
            model_name='post',
            name='photos',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='model', to='blog.photogallery'),
        ),
        migrations.AddField(
            model_name='photo',
            name='gallery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='blog.photogallery'),
        ),
    ]
