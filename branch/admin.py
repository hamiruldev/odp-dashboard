from django.contrib import admin
from .models import Master
from django.contrib.auth.admin import UserAdmin

from django.db import models
from django.forms import TextInput, Textarea, CharField
from django import forms



class BranchAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "is_hq")

admin.site.register(Master, BranchAdmin)

