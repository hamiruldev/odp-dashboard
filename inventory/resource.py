from import_export import resources
from .models import Inventory, Category, PropertyType

class ReportResourceInventory(resources.ModelResource):
    class Meta:
        model = Inventory

class ReportResourceCategory(resources.ModelResource):
    class Meta:
        model = Category
    
class ReportResourcePropertyType(resources.ModelResource):
    class Meta:
        model = PropertyType

        