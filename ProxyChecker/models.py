from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
# Create your models here.
"""
Proxy Socks5
added GoodProxys, BadProxys, LoadedProxys and PorxyContainer -models to Proxychecker; Proxychecker is only ckecking when the proxy is not in BadProxys and GoodProxy, DB-commits working, homeSection is showing only working Proxys now"

"""
# New Proxy Database for fast intteration

class ProxyCheckStamp(models.Model):
    added = models.DateTimeField(verbose_name="Added", default=timezone.now)
    checked = models.DateTimeField(verbose_name="Timestamp", blank=True, default="")
    protokol = models.CharField(max_length=16, blank=True)
    working = models.BooleanField(verbose_name="Bad or Good Proxy")
    def __str__(self):
        return self.checked

class Proxy(models.Model):
    ipaddress = models.GenericIPAddressField(verbose_name="IP-adress",protocol='IPv4')
    port = models.IntegerField(verbose_name="Port",default=None)
    ProxyCheckStamp = models.ForeignKey(ProxyCheckStamp, on_delete=models.CASCADE, default = 1 )
    protokol = models.CharField(max_length=16, blank=True)
    def __str__(self):
        return self.ipaddress


class BadProxyy(models.Model):
    address= models.ForeignKey('Proxy', on_delete=models.CASCADE)
    timestampAdded = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.address



class GoodProxyy(models.Model):
    address = models.ForeignKey('Proxy', on_delete=models.CASCADE)
    timestampAdded = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.address



class UserProxy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestampAdded = models.DateTimeField(default=timezone.now)
    timestampChecked = models.DateTimeField(default=timezone.now)
    email = models.EmailField(default="")
    protokol = models.CharField(max_length=16, blank=True)
    country = models.CharField(max_length=30,blank=True,default="DE")
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
    country = models.CharField(max_length=30,blank=True,default="DE")
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
    country = models.CharField(max_length=30,blank=True,default="DE")
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
    country = models.CharField(max_length=30,blank=True,default="")
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
    urlstring =models.URLField(verbose_name="URL",default="")
#    site = models.CharField(max_length=200, blank=True, default="")
    timestampAdded = models.DateTimeField(auto_now=timezone.now)
#    timestampChecked = models.DateTimeField(default="")
    def __str__(self):
        return "{0}".format(str(self.urlstring))





#class CSVFile(models.Model):
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    fileUpload= models.FileField(null=True)
