# branch/serializers.py
from rest_framework import serializers
from .models import Branch

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('id', 'name', 'location', 'is_hq', 'description', 'branch_commision_precent')

