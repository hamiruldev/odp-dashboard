# branch/models.py
from django.db import models
from django.contrib.auth.models import Group, Permission


class Master(models.Model):
    name = models.CharField(max_length=255, unique=True, primary_key=True)
    location = models.CharField(max_length=255, default='')
    is_hq = models.BooleanField(default=False)
    description = models.TextField()

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['location']

    def __str__(self):
        return self.name
        
    def save(self, *args, **kwargs):
        if not self.location:
            self.location = self.name.upper()
        super().save(*args, **kwargs)

