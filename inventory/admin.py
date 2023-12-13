from django.contrib import admin

from .models import Category, PropertyType, Inventory

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    model = Inventory
    search_fields = ('title', 'username', 'first_name',)
    list_filter = ('branch', )

admin.site.register(Category)
admin.site.register(PropertyType)
