# Generated by Django 4.0.3 on 2023-11-26 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='Enter group name (e.g. Cobra, Titan etc.)', max_length=255, null=True, unique=True)),
                ('empires', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('about', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
