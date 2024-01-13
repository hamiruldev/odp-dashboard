from rest_framework import serializers
from profiles.models import Profile
from users.models import NewUser
from teams.models import Team
from branchs.models import Branch

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# class UserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = UserProfile
#         fields = ('id', 'userId', 'nickname', 'firstName', 'lastName', 'photo', 'description',
#         'phone_no', 'email', 'top_seller', 'is_verified')

class CustomUserTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super(CustomUserTokenObtainPairSerializer, self).validate(attrs)
        data.update({'username': self.user.username})
        data.update({'email': self.user.email})
        data.update({'id': self.user.id})
        return data


class CustomUserSerializer(serializers.ModelSerializer):

    """
    Currently unused in preference of the below.
    """
    
    birth_date = serializers.DateField(required=True)
    branch = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    full_name = serializers.CharField(required=True)
    ic_no = serializers.CharField(required=True)
    ic_type = serializers.CharField(required=True)
    introducer = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)
    phone_no = serializers.CharField(required=True)
    team = serializers.CharField(required=True)
    username = serializers.CharField(required=True)
    
    class Meta:

        fields = ('email','phone_no', 'username','full_name', 'password', 'introducer', 'team', 'branch','birth_date','ic_no','ic_type' )
        extra_kwargs = {'password': {'write_only': True}}
        model = NewUser

    def validate(self, attrs):

        email = attrs.get('email', '')
        phone_no = attrs.get('phone_no', '')
        username = attrs.get('username', '')
        full_name = attrs.get('full_name', '')
        introducer = attrs.get('introducer', '')
        team = attrs.get('team', '')
        branch = attrs.get('branch', '')
        birth_date = attrs.get('birth_date', '')
        ic_no = attrs.get('ic_no', '')
        ic_type = attrs.get('ic_type', '')
        
        introducer_username = introducer
        if introducer_username:
            try:
                introducer = NewUser.objects.get(username=introducer_username)
            except NewUser.DoesNotExist:
                raise serializers.ValidationError({'introducer': "Introducer does not exist"})
            attrs['introducer'] = introducer
        
        team_name = team
        if team_name:
            try:
                team = Team.objects.get(name=team_name)
                
            except Team.DoesNotExist:
                raise serializers.ValidationError({'team': "team does not exist"})
            attrs['team'] = team
            
        branch_name = branch
        if branch_name:
            try:
                branch = Branch.objects.get(name=branch_name)
                
            except Branch.DoesNotExist:
                raise serializers.ValidationError({'branch': "branch does not exist"})
            attrs['branch'] = branch


        if NewUser.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': "Email is already in use"})
            
        if NewUser.objects.filter(email=phone_no).exists():
            raise serializers.ValidationError(
                {'phone_no': "No Phone is already in use"})

        if NewUser.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {'username': "Username is already in use"})

        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewUser
        fields = ('username', 'password','full_name', 'first_name' , 'introducer', 'team', 'branch', 'email', 'is_staff', 'is_active', 'about')
