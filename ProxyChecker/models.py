from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
# Create your models here.
import random
"""


"""
random.seed()

# New Proxy Database for fast iteration

class ProxyLocation(models.Model):
    # Location Entitys
    continent_code = models.CharField(max_length=2,blank=True, default="")
    continent_name = models.CharField(max_length=15,blank=True, default="")
    country_name = models.CharField(max_length=30,blank=True, default="")
    country_code = models.CharField(max_length=2,blank=True, default="")
    city = models.CharField(max_length=50,blank=True, default="")
    region = models.CharField(max_length=50,blank=True, default="")
    postal_code = models.CharField(max_length=14,blank=True, default="")
    dma_code = models.CharField(max_length=10,blank=True, default="")
    latitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    longitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    time_zone = models.CharField(max_length=20,blank=True, default="")

class BlackListed(models.Model):
    name = models.CharField(max_length=100)
    URL = models.URLField(verbose_name="B-list Provider", blank=True)
    listed = models.BooleanField(default=False)

class ProxyCheckStamp(models.Model):
    added = models.DateTimeField(verbose_name="Added", default=timezone.now)
    working = models.BooleanField(verbose_name="Bad or Good Proxy",default=False)
    checked = models.DateTimeField(verbose_name="Last check", blank=True, default="")
    # Proxy Credentials
    proxy_user = models.CharField(max_length=50,default="")
    proxy_pw = models.CharField(max_length=50,default="")
    email = models.EmailField(default="")
    # Meta-data
    PROTOKOLL_CHOICES = [
    (0, 'http'),
    (1, 'https'),
    (2, 'socks4'),
    (3, 'socks5'),
    (4, 'ssl'),
    (5, None)]
    ANONYMITY_CHOICES = (
    (0, 'elite'),
    (1, 'anonymous'),
    (2, 'high anonymous'),
    (3, 'transparent'),
    (4, 'none'))
    PREMIUM_CHOICES = (
    (0, 'None'),
    (1, 'free'),
    (2, 'premium'),
    (3, 'vrah-proxy-star'),
    (4, 'admin'))
    protokol = models.CharField(choices=PROTOKOLL_CHOICES, max_length=16, default=5)
    anonymity =  models.CharField(choices=ANONYMITY_CHOICES, max_length=16, blank=True)
    blackListed = models.ForeignKey(BlackListed, on_delete=models.CASCADE,blank=True, null=True)
    premiumStatus = models.CharField(choices=PREMIUM_CHOICES, max_length=16, blank=True)

    # Performance stats
    latenz = models.IntegerField(default=80)
    speed = models.IntegerField(default=80)
    def __str__(self):
        return self.checked


class Proxy_Port(models.Model):
    port = models.SmallIntegerField(verbose_name="Port",blank=True)
#    class Meta:
#        Ordering = ['port']
    def __str__(self):
        return self.port

class Proxy(models.Model):
    ipaddress = models.GenericIPAddressField(verbose_name="IP-adress",protocol='IPv4')
    port = models.ForeignKey(Proxy_Port, on_delete=models.CASCADE)
    checkerThreadLocked= models.BooleanField(verbose_name="Status Thread-locked ",default=False)
    ProxyCheckStamp = models.ForeignKey(ProxyCheckStamp, on_delete=models.CASCADE, blank=True)
    users = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    def __str__(self):
        return self.ipaddress, self.port


class ProxyStringUrl(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    urlstring =models.URLField(verbose_name="URL",default="")
    timestampAdded = models.DateTimeField(auto_now=timezone.now)
    #    timestampChecked = models.DateTimeField(default="")
    def __str__(self):
        return "{0}".format(str(self.urlstring))

class UserProxy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestampAdded = models.DateTimeField(default=timezone.now)
    timestampChecked = models.DateTimeField(default=timezone.now)
    email = models.EmailField(default="")
    protokol = models.CharField(max_length=16, blank=True)
    country = models.CharField(max_length=30,blank=True,default="DE")
    countryCode = models.CharField(max_length=2,blank=True,default="DE")
    onlineStatus = models.BooleanField(default=False)
    anonymity = models.CharField(verbose_name="Anonymity",blank=True, max_length=14,default="none")
    latenz = models.FloatField(default=80)
    speed = models.IntegerField(default=80)
    ipAdress = models.GenericIPAddressField(default="")
    port = models.IntegerField(blank=True)
    def __str__(self):
        return "{1}:{2} {3} {0} {4} {5}".format(self.protokol ,self.ipAdress, self.port, self.email,self.anonymity, self.country)

class GoodProxy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestampAdded = models.DateTimeField(default=timezone.now)
    timestampChecked = models.DateTimeField(default=timezone.now)
    email = models.EmailField(default="")
    protokol = models.CharField(max_length=16, blank=True)
    country = models.CharField(max_length=30,blank=True,default="DE")
    countryCode = models.CharField(max_length=2,blank=True,default="DE")
    onlineStatus = models.BooleanField(default=False)
    anonymity = models.CharField(blank=True, max_length=14,default="none")
    latenz = models.FloatField(default=0)
    speed = models.IntegerField(default=0)
    ipAdress = models.GenericIPAddressField(default="0.0.0.0")
    port = models.IntegerField(blank=True)
    def __str__(self):
        return "{1}:{2} {3} {0} {4} {5} {6}".format(self.protokol ,self.ipAdress, self.port, self.email,self.anonymity, self.country, self.latenz, self.timestampAdded, self.timestampChecked)

class BadProxy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestampAdded = models.DateTimeField(default=timezone.now)
    timestampChecked = models.DateTimeField(null=True)
    email = models.EmailField(default="")
    protokol = models.CharField(max_length=16, blank=True)
    country = models.CharField(max_length=30,blank=True,default="")
    countryCode = models.CharField(max_length=2,blank=True,default="")
    onlineStatus = models.BooleanField(default=False)
    anonymity = models.CharField(blank=True, max_length=14, default="none")
    latenz = models.FloatField(default=0)
    speed = models.IntegerField(default=0)
    ipAdress = models.GenericIPAddressField(default="")
    port = models.IntegerField(default=0)
    def __str__(self):
        return "{1}:{2} {3} {0} {4} {5} {6}".format(self.protokol ,self.ipAdress, self.port, self.email,self.anonymity, self.country, self.latenz)






#class CSVFile(models.Model):
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    fileUpload= models.FileField(null=True)
