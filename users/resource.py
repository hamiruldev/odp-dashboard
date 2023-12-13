from import_export import resources
from .models import NewUser

class ReportResource(resources.ModelResource):
    class Meta:
        model = NewUser