import json
from django.http import HttpResponse, JsonResponse
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from users.models import NewUser

from .serializers import CustomUserSerializer, CustomUserTokenObtainPairSerializer, UserSerializer
from profiles.models import Profile
from profiles.serializers import UserProfileSerializer

# from django.shortcuts import get_object_or_404

from rest_framework import generics

# from django.core.mail import send_mail

from django.core.mail import send_mail, EmailMultiAlternatives

import random

from django.conf import settings


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from users.admin import CustomUserCreationForm  # Import your custom form


class CustomUserRegistration(generics.RetrieveUpdateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            profile = Profile()
            profile.user = user
            profile.first_name = user.first_name
            profile.last_name = user.last_name
            profile.email = user.email
            profile.phone_no = user.phone_no
            profile.introducer = user.introducer
            # profile.team = Profile().get_team_id()
            profile.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomUserTokenObtainPairSerializer


class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CustomResetPassword(generics.RetrieveUpdateAPIView):

    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    # serializer = CustomUserSerializer(data=request.data)

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('username')
        user = get_object_or_404(NewUser, username=item)
        email = user.email

        rand = random.randint(1000, 2000)

        tempPass = str(rand)

        user.set_password(tempPass)
        user.save()

        subject, from_email, to = 'Reset Password', 'web.onedreamproperty@gmail.com', email,
        url = settings.BASE_URL_FE

        text_content = 'This is an important message.'
        html_content = '<p>This is a <strong> temporary link reset password : </strong> <a href=' + url + 'reset/?tem=' + \
            tempPass + '&user=' + item + '> ' + tempPass + ' </a></p>'
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        return get_object_or_404(NewUser, username=item)


class CustomNewPassword(generics.RetrieveUpdateAPIView):

    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, **kwargs):

        item = self.kwargs.get('temPass')
        username = self.kwargs.get('username')
        user = get_object_or_404(NewUser, username=username)

        if user.check_password(item):
            dataBody = request.data["password"]

            user.set_password(dataBody)
            user.save()
            userJson = UserSerializer(user)

            return JsonResponse(userJson.data, status=201)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # return redirect('home')  # Replace 'home' with the URL name of your home page
            return redirect('admin')  # Replace 'home' with the URL name of your home page
    else:
        form = CustomUserCreationForm()

    return render(request, 'admin/registration/signup.html', {'form': form})
