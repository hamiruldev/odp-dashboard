from django.contrib import admin
from users.models import NewUser
from profiles.models import Profile
from django.contrib.auth.models import Group

from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models
from django.urls import reverse
from django.utils.html import format_html
from django.shortcuts import get_list_or_404
from django.db.models import Sum

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from import_export.admin import ImportExportModelAdmin
from .resource import ReportResource


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = NewUser
        fields = ('email', 'username', 'first_name', 'introducer', 'branch', 'team')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = NewUser
        fields = ('email', 'username', 'first_name', 'is_active', 'is_staff', 'user_view', 'introducer', 'branch', 'team')


class UserAdminConfig(UserAdmin, ImportExportModelAdmin):
    resource_class = ReportResource
    model = NewUser
    search_fields = ('email', 'username', 'first_name',)
    list_filter = ('team', 'branch',)
    ordering = ('-user_profile__view_count',)
    list_display = ('username_link', 'user_profile_link', 'introducer', 'branch', 'team', 'is_active', 'get_group_names')
    autocomplete_fields = ['introducer']

    
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                        'email',
                        'username',
                        'password1', 'password2',
                        'groups'),
            },
         ),
        (("Personal info"), {"fields": ("first_name", "last_name", 'is_active', 'is_staff')}),
        (("Referal"), {"fields": ("introducer", "team", "branch")}),
    )

    fieldsets = (
        (None, {
            'fields': (
                'email',
                'username',
                'password',
            ),
        }),
        (("Personal info"), {
            'fields': (
                "first_name",
                "last_name",
                'is_active',
                'is_staff',
            ),
        }),
        (("Referral"), {
            'fields': (
                "introducer",
                "team",
                "branch",
            ),
        }),
        (("Important dates"), {
            'fields': (
                'last_login',
                'date_joined',
            ),
        }),
    )
    

    def username_link(self, obj):
        url = reverse('admin:{}_{}_change'.format(
            obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        return format_html('<a href="{}">{}</a>', url, obj.username)

    def user_profile_link(self, obj):
        profile_url = "https://onedreamproperty.com.my/{}".format(
            obj.username)
        return format_html('<a href="{}" target="_blank">{}</a>', profile_url, obj.username)

    def user_view(self, obj):
        total_view_count = Profile.objects.filter(
            user__username=obj.username).aggregate(Sum('view_count'))['view_count__sum']

        if total_view_count is not None:
            return total_view_count
        else:
            return 0

    def get_group_names(self, obj):
        return ", ".join([group.name for group in obj.groups.all()])

    get_group_names.short_description = 'Groups'

    user_profile_link.short_description = 'User Link'
    username_link.short_description = 'User Name'
    user_view.short_description = 'User view'
    user_view.admin_order_field = 'user_profile__view_count'


admin.site.register(NewUser, UserAdminConfig)
