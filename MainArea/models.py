from django.db import models
from django.contrib.auth.models import User
from ProxyChecker.models import Proxy


class UserProxys(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ownProxy  = models.ManyToManyField(Proxy)
    addedFromUser = models.DateTimeField(auto_now_add=True)
    # proxy = models.ForeignKey
    def __str__(self):
        return self.user

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="user_profile")
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    timestampAdded = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return self.name
