from django.db import models
from django.contrib.auth.models import User
# Create your models here.
"""
Proxy Soscks5












"""

class UserProxy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestampAdded = models.DateTimeField(auto_now=True)
    timestampUpdated = models.DateTimeField(auto_now=True)

    protokol = models.CharField(max_length=6, blank=True)
    country = models.CharField(max_length=10,blank=True)
    onlineStatus = models.BooleanField(default=False,)
    anonymitaetsLevel = models.CharField(verbose_name="Anonymous Level",max_length=14,blank=True)
    latenz = models.FloatField(blank=True)
    speed = models.IntegerField(blank=True, default=0)

    ipAdress = models.GenericIPAddressField()
    port = models.IntegerField(blank=True)
    def __str__():
        return self.ipAdress
