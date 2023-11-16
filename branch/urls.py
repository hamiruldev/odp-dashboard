# branch/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MasterViewSet

app_name = 'branch'

router = DefaultRouter()
router.register(r'masters', MasterViewSet, basename='master')

urlpatterns = [
    path('api/', include(router.urls)),
]