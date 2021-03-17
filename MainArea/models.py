from django.db import models
from django.contrib.auth.models import User


class ProxyContainer(models.Model):

    tutorial_title = models.CharField(max_length=200)
    ipAdress = models.GenericIPAddressField(blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    port1 = models.IntegerField(blank=True, null=True)
    port2 = models.IntegerField(blank=True, null=True)
    port3 = models.IntegerField(blank=True, null=True)

    country = models.CharField(blank=True,max_length=45)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField('date published')

    def __str__(self):
        return self.ipAdress

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
