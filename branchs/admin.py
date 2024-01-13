from django.contrib import admin
from .models import Branch
from django.contrib.auth.admin import UserAdmin

from django.db import models
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.http import JsonResponse
from django.template.response import TemplateResponse
import environ
class BranchAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "is_hq", 'branch_commision_precent')
    change_list_template = 'admin/branchs/branch/change_list.html'
    search_fields=('branchs',)

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context)
        queryset = self.get_queryset(request)
        env = environ.Env()

        branches_data = [
            {'lat': branch.lat, 'long': branch.long, 'name': branch.name}
            for branch in queryset
        ]

        if isinstance(response, TemplateResponse):
            response.context_data['branches_json'] = branches_data
            response.context_data['mapboxglToken'] = env('SECRET_KEY_MAP_BOX')

        return response

admin.site.register(Branch, BranchAdmin)
admin.site.index_title = 'Branch'

