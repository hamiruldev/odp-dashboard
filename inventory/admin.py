from django.contrib import admin

from .models import Category, PropertyType, Inventory

from import_export.admin import ImportExportModelAdmin
from .resource import ReportResourceInventory, ReportResourceCategory, ReportResourcePropertyType

class InventoryAdmin(ImportExportModelAdmin):
    resource_class = ReportResourceInventory
    model = Inventory
    list_display = ("title", "view_count", "inventory_date", )
    search_fields = ('title', 'username', 'first_name',)
    list_filter = ('branch', )
    ordering = ('-inventory_date',)


class CategoryAdmin(ImportExportModelAdmin):
    resource_class = ReportResourceCategory
    model = Category

class PropertyTypeAdmin(ImportExportModelAdmin):
    resource_class = ReportResourcePropertyType
    model = PropertyType

admin.site.register(Category, CategoryAdmin)
admin.site.register(PropertyType, PropertyTypeAdmin)
admin.site.register(Inventory, InventoryAdmin)

