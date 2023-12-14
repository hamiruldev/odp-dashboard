# branch/models.py
from django.db import models
from django.contrib.auth.models import Group, Permission
from django.urls import reverse

import environ
import geocoder

# Read the .env file
env = environ.Env()

class Branch(models.Model):
    name = models.CharField(max_length=255, unique=True, null=True, default='', help_text="Enter branch name (e.g. Cobra, Tycoon etc.)")
    
    location = models.CharField(max_length=255, default='', help_text="Enter branch name (e.g. Damansara Alif, Add Height etc.)" )

    lat = models.CharField(max_length = 20,null=True,blank=True)
    long=models.CharField(max_length = 20,null=True,blank=True)

    is_hq = models.BooleanField(default=False)
    description = models.TextField(default='', null=True, blank=True)

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.location, key=env('SECRET_KEY_MAP_BOX'))
        dict=list(g.latlng)
        self.lat=dict[0]
        self.long=dict[1]
        super(Branch, self).save(*args, **kwargs)

    def __str__(self):
        return self.name