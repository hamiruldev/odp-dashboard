from django.urls import path

from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.ProfileView.as_view(), name='profile-view'),
    path('<str:username>', views.ProfileDetail.as_view(), name='profile-detail'),
]