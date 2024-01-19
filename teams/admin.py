from django.contrib import admin
from .models import Team
from django.contrib.auth.admin import UserAdmin

from django.db import models
from django.forms import TextInput, Textarea, CharField
from django import forms

from django.template.response import TemplateResponse


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'founder', 'about', 'calculate_empire', 'team_commision_precent')
    change_list_template = 'admin/teams/team/change_list.html'
    autocomplete_fields = ['founder']
    search_fields=('name',)
    

    def calculate_empire(self, obj):
        from users.models import NewUser

        total_user = NewUser.objects.filter(team=obj).count()
        return total_user

    calculate_empire.short_description = 'Empires'

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context)

        if isinstance(response, TemplateResponse):
            queryset = self.get_queryset(request)
            team_data = [
                {'name': team.name, 'founder': team.founder.username, 'empires': self.calculate_empire(team), 'team_commision_precent': team.team_commision_precent}
                for team in queryset
            ]

            response.context_data['team_data'] = team_data

        return response

admin.site.register(Team, TeamAdmin)
