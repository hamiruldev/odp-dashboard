from django.contrib import admin

from .models import Category, PropertyType, Inventory

from import_export.admin import ImportExportModelAdmin
from .resource import ReportResource

class InventoryAdmin(ImportExportModelAdmin):
    resource_class = ReportResource
    model = Inventory
    search_fields = ('title', 'username', 'first_name',)
    list_filter = ('branch', )

admin.site.register(Category)
admin.site.register(PropertyType)
admin.site.register(Inventory, InventoryAdmin)

