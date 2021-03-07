from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
# Create your models here.
"""
Proxy Socks5

"""

class UserProxy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestampAdded = models.DateTimeField(default=timezone.now)
    timestampUpdated = models.DateTimeField(default=timezone.now)
    email = models.EmailField(blank=True)
    protokol = models.CharField(max_length=6, blank=True,default="High")
    country = models.CharField(max_length=10,blank=True,default="DE")
    onlineStatus = models.BooleanField(default=False)
    anonymitaetsLevel = models.CharField(blank=True, max_length=14,default="High")
    latenz = models.FloatField(blank=True)
    speed = models.IntegerField(blank=True)
    ipAdress = models.GenericIPAddressField(default="0.0.0.0")
    port = models.IntegerField(blank=True,default=8080)

    def __str__(self):
        return self.protokol ,self.ipAdress, self.port, self.email


#class CSVFile(models.Model):
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    fileUpload= models.FileField(null=True)
