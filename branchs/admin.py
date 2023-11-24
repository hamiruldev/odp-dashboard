from django.contrib import admin
from .models import Branch
from django.contrib.auth.admin import UserAdmin

from django.db import models
from django.forms import TextInput, Textarea, CharField
from django import forms



class BranchAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "is_hq")
    order = 1

admin.site.register(Branch, BranchAdmin)
admin.site.index_title = 'Branch'

