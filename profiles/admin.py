from django.contrib import admin

from .models import Profile
from .resource import ReportResourceProfile
from import_export.admin import ImportExportModelAdmin


class ProfileAdmin(ImportExportModelAdmin):
    list_display = ("user", "view_count",)
    
    resource_class = ReportResourceProfile
    autocomplete_fields = ['user']


admin.site.register(Profile, ProfileAdmin)