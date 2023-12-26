from django.contrib import admin

from django.utils.html import format_html

from .models import Category, PropertyType, Inventory

from import_export.admin import ImportExportModelAdmin
from .resource import ReportResourceInventory, ReportResourceCategory, ReportResourcePropertyType

class InventoryAdmin(ImportExportModelAdmin):
    resource_class = ReportResourceInventory
    model = Inventory
    list_display = ("display_feature_image", "title", "view_count", "inventory_date",)
    search_fields = ('title', 'branch', )
    list_filter = ('branch', )
    ordering = ('-inventory_date',)
    # autocomplete_fields = ('realtor', 'branch')
    
    def display_feature_image(self, obj):
        
        fallback_image_path = '/media/no_image/no_image.jpeg'
        
        if obj.featureImage:
            return format_html('<img src="{}" style="max-height:100px; max-width:100px;" onerror="this.src=\'' + fallback_image_path + '\'" />', obj.featureImage.url)
        else:
            return 'No Image'

    display_feature_image.short_description = 'Feature Image'
    


class CategoryAdmin(ImportExportModelAdmin):
    resource_class = ReportResourceCategory
    model = Category

class PropertyTypeAdmin(ImportExportModelAdmin):
    resource_class = ReportResourcePropertyType
    model = PropertyType

admin.site.register(Category, CategoryAdmin)
admin.site.register(PropertyType, PropertyTypeAdmin)
admin.site.register(Inventory, InventoryAdmin)

