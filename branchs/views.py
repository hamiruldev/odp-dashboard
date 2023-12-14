# branch/views.py
from rest_framework import viewsets
from .models import Branch
from .serializers import BranchSerializer

from django.shortcuts import render, get_object_or_404
from .models import Branch

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
