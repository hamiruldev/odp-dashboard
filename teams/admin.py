from django.contrib import admin
from .models import Team
from django.contrib.auth.admin import UserAdmin

from django.db import models
from django.forms import TextInput, Textarea, CharField
from django import forms

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name','founder', 'about', 'empires')

admin.site.register(Team, TeamAdmin)

