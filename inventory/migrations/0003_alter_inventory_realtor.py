# Generated by Django 4.0.3 on 2022-04-12 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_lastname_alter_profile_nickname_and_more'),
        ('inventory', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='realtor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventories', to='profiles.profile'),
        ),
    ]
