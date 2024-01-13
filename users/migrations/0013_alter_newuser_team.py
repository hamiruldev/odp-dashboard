# Generated by Django 4.0.3 on 2024-01-05 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_alter_team_name'),
        ('users', '0012_alter_newuser_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='team',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.SET_NULL, to='teams.team'),
        ),
    ]
