# branch/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BranchViewSet

app_name = 'branchs'

router = DefaultRouter()
router.register(r'branch', BranchViewSet, basename='branch')

urlpatterns = [
    path('api/', include(router.urls)),
]