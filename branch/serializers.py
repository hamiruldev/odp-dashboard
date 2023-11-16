# branch/serializers.py
from rest_framework import serializers
from .models import Master

class MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = ('name', 'location', 'is_hq', 'description')

