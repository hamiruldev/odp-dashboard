from django.contrib import admin

from .models import Category, PropertyType, Inventory

from import_export.admin import ImportExportModelAdmin
from .resource import ReportResourceInventory, ReportResourceCategory, ReportResourcePropertyType
import environ
from django.template.response import TemplateResponse


class InventoryAdmin(ImportExportModelAdmin):
    resource_class = ReportResourceInventory
    model = Inventory
    change_list_template = 'admin/inventorys/inventory/change_list.html'
    change_form_template = 'admin/inventorys/inventory/change_form.html'
    list_display = ("title", 'city','category', "view_count", "inventory_date", 'location' )
    search_fields = ('title', 'city',)
    list_filter = ('category','branch', )
    ordering = ('-inventory_date',)
    
    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context)
        queryset = self.get_queryset(request)
        env = environ.Env()
        
        inventorys_data = [
            {
                'id' : inventory.id,
                'lat': float(inventory.lat) if inventory.lat is not None else '',
                'long': float(inventory.long) if inventory.long is not None else '',
                'location': inventory.location if inventory.location is not None else '',
                'title': inventory.title,
                'feature_image': 'https://onedream.dynamicdigital.guru' + inventory.featureImage.url if inventory.featureImage else '',  # Use the 'url' attribute
            }
            for inventory in queryset
        ]        
                        
        if isinstance(response, TemplateResponse):
            response.context_data['inventorys_json'] = inventorys_data
            response.context_data['mapboxglToken'] = env('SECRET_KEY_MAP_BOX')

        return response


class CategoryAdmin(ImportExportModelAdmin):
    resource_class = ReportResourceCategory
    model = Category

class PropertyTypeAdmin(ImportExportModelAdmin):
    resource_class = ReportResourcePropertyType
    model = PropertyType

admin.site.register(Category, CategoryAdmin)
admin.site.register(PropertyType, PropertyTypeAdmin)
admin.site.register(Inventory, InventoryAdmin)

