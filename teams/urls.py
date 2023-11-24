# branch/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet

app_name = 'teams'

router = DefaultRouter()
router.register(r'team', TeamViewSet, basename='team')

urlpatterns = [
    path('api/', include(router.urls)),
]