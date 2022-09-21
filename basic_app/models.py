from distutils.command.upload import upload
from django.contrib.auth.hashers import Argon2PasswordHasher

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pics = models.ImageField(upload_to='profile_pics',blank=True)
    portfolio_site = models.URLField(blank=True)

    def __str__(self):
        return self.user.username