from rest_framework import serializers

from profiles.models import Profile
from users.models import NewUser

class UserProfileSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source='user.username', required=False)

    class Meta:
        model = Profile
        fields = ('username', 'user', 'photo', 'nickname', 'first_name', 'last_name', 'description', 'phone_no', 'email',
                  'facebook', 'instagram', 'youtube', 'linkedin', 'tiktok', 'is_verified', 'is_agent', 'view_count'
                  )

class IntroducerSerializer(serializers.ModelSerializer):
    
    branch_name = serializers.CharField(source='branch.name', read_only=True)
    branch_id = serializers.IntegerField(source='branch.id', read_only=True)
    
    team_name = serializers.CharField(source='team.name', read_only=True)
    team_id = serializers.IntegerField(source='team.id', read_only=True)

    photo = serializers.ImageField(source='user_profile.photo', read_only=True)
    description = serializers.CharField(source='user_profile.description', read_only=True)

    class Meta:
        model = NewUser
        fields = ( 'id', 'photo', 'description', 'first_name', 'last_name', 'phone_no', 'email', 'branch_name','branch_id', 'team_id', 'team_name', 'is_agent')
        
        

