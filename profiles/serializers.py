from rest_framework import serializers

from profiles.models import Profile
from users.models import NewUser


class UserProfileSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source='user.username', required=False)

    class Meta:
        model = Profile
        fields = ('username', 'user', 'photo', 'nickname', 'firstName', 'lastName', 'description', 'phone', 'email',
                  'facebook', 'instagram', 'youtube', 'linkedin', 'tiktok', 'is_verified', 'view_count'
                  )
