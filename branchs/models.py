# branch/models.py
from django.db import models
from django.contrib.auth.models import Group, Permission
from django.urls import reverse


class Branch(models.Model):
    name = models.CharField(max_length=255, unique=True, null=True, default='', help_text="Enter branch name (e.g. Damansara Alif, Add Height etc.)")
    
    location = models.CharField(max_length=255, default='')
    is_hq = models.BooleanField(default=False)
    description = models.TextField(default='', null=True, blank=True)

    # USERNAME_FIELD = 'name'
    # REQUIRED_FIELDS = ['location']

    def __str__(self):
        return self.name
        
    def save(self, *args, **kwargs):
        if not self.location:
            self.location = self.name.upper()
        super().save(*args, **kwargs)
