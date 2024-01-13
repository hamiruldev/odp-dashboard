from django.contrib import admin

from .models import Profile
from .resource import ReportResourceProfile
from import_export.admin import ImportExportModelAdmin
from django.template.response import TemplateResponse


class ProfileAdmin(ImportExportModelAdmin):
    list_display = ("user", "view_count", 'introducer_total',)
    
    resource_class = ReportResourceProfile
    autocomplete_fields = ['user']
    exclude = ('group_id', 'first_name')
        
    search_fields = ('user__username',)
    
    
    def calculate_introducer_total(self, obj):
        from users.models import NewUser        

        total_user = NewUser.objects.filter(introducer=obj.user).count()
        
        obj.introducer_total = total_user
        obj.save()


        return total_user

    calculate_introducer_total.short_description = 'Introducer'

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context)

        if isinstance(response, TemplateResponse):
            queryset = self.get_queryset(request)
            profile_data = [
                {'user': profile.user, 'view_count': profile.view_count, 'introducer_total': self.calculate_introducer_total(profile)}
                for profile in queryset
            ]

            response.context_data['profile_data'] = profile_data            

        return response

    
admin.site.register(Profile, ProfileAdmin)