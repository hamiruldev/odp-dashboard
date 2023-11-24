# Generated by Django 4.0.3 on 2023-11-23 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('name', models.CharField(default='', help_text='Enter group name (e.g. Cobra, Titan etc.)', max_length=255, primary_key=True, serialize=False, unique=True)),
                ('empires', models.PositiveIntegerField(default=0, null=True)),
                ('about', models.TextField()),
            ],
        ),
    ]
