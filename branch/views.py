# branch/views.py
from rest_framework import viewsets
from .models import Master
from .serializers import MasterSerializer

class MasterViewSet(viewsets.ModelViewSet):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer
