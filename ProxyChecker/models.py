from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
# Create your models here.
import random
"""
Proxy Socks5
added GoodProxys, BadProxys, LoadedProxys and PorxyContainer -models to Proxychecker; Proxychecker is only ckecking when the proxy is not in BadProxys and GoodProxy, DB-commits working, homeSection is showing only working Proxys now"

"""
random.seed()

# New Proxy Database for fast iteration

class ProxyLocation(models.Model):
    # Location Entitys
    country = models.CharField(max_length=30,blank=True, default="--")
    countryCode = models.CharField(max_length=2,blank=True, default="")
    zipcode = models.CharField(max_length=14,blank=True, default="")
    city = models.CharField(max_length=50,blank=True, default="")
    Latitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    Longitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)

class BlackListed(models.Model):
    name = models.CharField(max_length=100)
    URL = models.URLField(verbose_name="B-list Provider", blank=True)
    listed = models.BooleanField(default=False)

class ProxyCheckStamp(models.Model):
    added = models.DateTimeField(verbose_name="Added", default=timezone.now)
    working = models.BooleanField(verbose_name="Bad or Good Proxy")
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
