# teams/models.py
from django.db import models
from django.contrib.auth.models import Group, Permission
# from users.models import NewUser
from django.conf import settings


class Team(models.Model):
    name = models.CharField(max_length=255, unique=True, null=True, default='', help_text="Enter group name (e.g. Cobra, Titan etc.)")
    founder = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='', related_name='founder_id')
    # co_founder = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='co_founder_id')
  
    
    empires = models.PositiveIntegerField(default=0, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    team_commision_precent = models.IntegerField(null=True,blank=True, default=0, verbose_name="Precent %")
    
    def __str__(self):
        return self.name

