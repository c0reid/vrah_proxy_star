from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
# Create your models here.
"""
Proxy Socks5
added GoodProxys, BadProxys, LoadedProxys and PorxyContainer -models to Proxychecker; Proxychecker is only ckecking when the proxy is not in BadProxys and GoodProxy, DB-commits working, homeSection is showing only working Proxys now"

"""

class UserProxy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestampAdded = models.DateTimeField(default=timezone.now)
    timestampChecked = models.DateTimeField(default=timezone.now)
    email = models.EmailField(default="")
    protokol = models.CharField(max_length=16, blank=True)
    country = models.CharField(max_length=20,blank=True,default="DE")
    countryCode = models.CharField(max_length=2,blank=True,default="DE")
    onlineStatus = models.BooleanField(default=False)
    anonymitaetsLevel = models.CharField(blank=True, max_length=14,default="none")
    latenz = models.FloatField(default=0)
    speed = models.IntegerField(default=0)
    ipAdress = models.GenericIPAddressField(default="")
    port = models.IntegerField(blank=True)
    def __str__(self):
        return "{1}:{2} {3} {0} {4} {5}".format(self.protokol ,self.ipAdress, self.port, self.email,self.anonymitaetsLevel, self.country)


class LoadedPrxy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestampAdded = models.DateTimeField(default=timezone.now)
    timestampChecked = models.DateTimeField(default=timezone.now)
    email = models.EmailField(default="")
    protokol = models.CharField(max_length=16, blank=True)
    country = models.CharField(max_length=20,blank=True,default="DE")
    countryCode = models.CharField(max_length=2,blank=True,default="DE")
    onlineStatus = models.BooleanField(default=False)
    anonymitaetsLevel = models.CharField(blank=True, max_length=14,default="none")
    latenz = models.FloatField(default=0)
    speed = models.IntegerField(default=0)
    ipAdress = models.GenericIPAddressField(default="")
    port = models.IntegerField(blank=True)
    def __str__(self):
        return "{1}:{2} {3} {0} {4} {5} {6}".format(self.protokol ,self.ipAdress, self.port, self.email,self.anonymitaetsLevel, self.country, self.latenz)




class GoodProxy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestampAdded = models.DateTimeField(default=timezone.now)
    timestampChecked = models.DateTimeField(default=timezone.now)
    email = models.EmailField(default="")
    protokol = models.CharField(max_length=16, blank=True)
    country = models.CharField(max_length=20,blank=True,default="DE")
    countryCode = models.CharField(max_length=2,blank=True,default="DE")
    onlineStatus = models.BooleanField(default=False)
    anonymitaetsLevel = models.CharField(blank=True, max_length=14,default="none")
    latenz = models.FloatField(default=0)
    speed = models.IntegerField(default=0)
    ipAdress = models.GenericIPAddressField(default="0.0.0.0")
    port = models.IntegerField(blank=True)
    def __str__(self):
        return "{1}:{2} {3} {0} {4} {5} {6}".format(self.protokol ,self.ipAdress, self.port, self.email,self.anonymitaetsLevel, self.country, self.latenz, self.timestampAdded, self.timestampChecked)

class BadProxy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestampAdded = models.DateTimeField(default=timezone.now)
    timestampChecked = models.DateTimeField(null=True)
    email = models.EmailField(default="")
    protokol = models.CharField(max_length=16, blank=True)
    country = models.CharField(max_length=20,blank=True,default="")
    countryCode = models.CharField(max_length=2,blank=True,default="")
    onlineStatus = models.BooleanField(default=False)
    anonymitaetsLevel = models.CharField(blank=True, max_length=14,default="none")
    latenz = models.FloatField(default=0)
    speed = models.IntegerField(default=0)
    ipAdress = models.GenericIPAddressField(default="")
    port = models.IntegerField(default=0)
    def __str__(self):
        return "{1}:{2} {3} {0} {4} {5} {6}".format(self.protokol ,self.ipAdress, self.port, self.email,self.anonymitaetsLevel, self.country, self.latenz)

class ProxyStringUrl(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    urlstring =models.URLField(verbose_name="Proxy-URLs",default="")
    site = models.CharField(max_length=16, blank=True)
    timestampAdded = models.DateTimeField(default=timezone.now)
    timestampChecked = models.DateTimeField(null=True)

    def __str__(self):
        return self.urlstring, self.user




#class CSVFile(models.Model):
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    fileUpload= models.FileField(null=True)
