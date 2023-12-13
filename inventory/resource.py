from import_export import resources
from .models import Inventory

class ReportResource(resources.ModelResource):
    class Meta:
        model = Inventory