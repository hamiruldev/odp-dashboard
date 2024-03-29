from django.forms import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, filters, status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser

from profiles.models import Profile
from users.models import NewUser
from branchs.models import Branch

from .serializers import UserProfileSerializer, IntroducerSerializer
from .permissions import ProfileUserWritePermission

# own user view and create


class ProfileView(generics.ListCreateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = None

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Profile.objects.filter(realtor=user)
        return Profile.objects.all()


class ProfileDetail(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [ProfileUserWritePermission]

    def get_object(self, queryset=None, **kwargs):
        username = self.kwargs.get('username')
        profile = get_object_or_404(Profile, user__username=username)

        # Update the view count on each visit to this post.
        if profile:
            # profile.view_count = profile.view_count + 1
            # profile.save()

            # Or
            profile.update_views()

        return get_object_or_404(Profile, user__username=username)

class IntroducerDetail(generics.RetrieveUpdateAPIView):
    serializer_class = IntroducerSerializer

    def get_object(self, queryset=None, **kwargs):
        username = self.kwargs.get('username')
        user = get_object_or_404(NewUser, username=username)
        profile = get_object_or_404(Profile, user=user.id)        
                
        user.photo = profile.photo
        user.description = profile.description
        
        
        return user
