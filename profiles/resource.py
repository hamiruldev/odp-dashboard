from import_export import resources
from .models import Profile

class ReportResourceProfile(resources.ModelResource):
    class Meta:
        model = Profile
        import_id_fields = ('user',)
        exclude = ('id',)