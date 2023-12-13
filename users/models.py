from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from branchs.models import Branch
from teams.models import Team
from django.urls import reverse
# from django.contrib.admin import Group

def get_upload_path(instance, filename):
    if instance:
        return f'logoUrl/user_{instance.name}/{filename}'


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, username, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, username, first_name, password, **other_fields)

    def create_user(self, email, username, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    # user_usernamename = models.CharField(max_length=150, unique=True)
    
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        default='',
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    
    serialize_username = models.CharField(
        max_length=150, default='', unique=False)

    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    introducer = models.CharField(max_length=200, null=True, blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, default=None, blank=True) 
    # group = model.TextChoices(Group)
    
    user_view = models.IntegerField(default=0, null=True, blank=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.serialize_username:
            self.serialize_username = self.username.upper()
        super().save(*args, **kwargs)


# class Group(models.Model):
#     name = models.CharField(max_length=100)
#     logoUrl = models.ImageField(
#         _("LogoUrl"), upload_to=get_upload_path, blank=True, null=True)
#     empires = models.PositiveIntegerField()
#     branch = models.CharField(max_length=100)
#     founder = models.CharField(max_length=100)
