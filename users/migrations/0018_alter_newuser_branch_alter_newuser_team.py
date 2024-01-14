# Generated by Django 4.0.3 on 2024-01-14 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('branchs', '0005_alter_branch_branch_commision_precent'),
        ('teams', '0005_team_team_commision_precent'),
        ('users', '0017_alter_newuser_introducer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='branch',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='branchs.branch'),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='team',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='teams.team'),
        ),
    ]