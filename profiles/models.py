from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from users.models import NewUser
from django.conf import settings


def get_upload_path(instance, filename):
    if instance:
        return f'profile_photo/user_{instance.user.username}/{filename}'


class Profile(models.Model):
    user = models.OneToOneField(
        NewUser, on_delete=models.CASCADE, related_name="user_profile", primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True)
    photo = models.ImageField(
        upload_to=get_upload_path, default="profile_photo/avatar.png")
    phone_no = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=100)


    nickname = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(blank=True)
    facebook = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)
    youtube = models.URLField(max_length=200, null=True, blank=True)
    tiktok = models.URLField(max_length=200, null=True, blank=True)
    linkedin = models.URLField(max_length=200, null=True, blank=True)

    top_seller = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=True)
    
    
    date_hired = models.DateTimeField(default=timezone.now, blank=True)
    view_count = models.IntegerField(default=0, blank=True)
    group_id = models.IntegerField(default=0)
    
    introducer_total = models.IntegerField(default=0, blank=True)
    
        # Add introducer field
    introducer = models.ForeignKey(
        NewUser, on_delete=models.SET_NULL, null=True, blank=True)


    
    def __str__(self):
        return self.email

    # An alternative to use to update the view count

    def update_views(self, *args, **kwargs):
        self.view_count = self.view_count + 1
        super(Profile, self).save(*args, **kwargs)

    def get_introducer_metadata(self, *args, **kwargs):
        try:
            introducerData = NewUser.objects.get(username=self.introducer)
            team = introducerData.team if introducerData.team else None
            return {
                'username': introducerData.username,
                'team': team
            }
        except NewUser.DoesNotExist:
            return None

    def get_team_id(self, *args, **kwargs):
        introducer_data = self.get_introducer_metadata()
        if introducer_data:
            return introducer_data.get('team')
        return None
