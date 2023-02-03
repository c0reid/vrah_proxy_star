import django_filters

from .models import *
from ProxyChecker.models import *


class ProxyFilter(django_filters.FilterSet):
    pass
    class Meta:
        model = GoodProxy
        exclude = ['user','timestampAdded','timestampChecked','email','countryCode','onlineStatus','speed','ipAdress','latenz', ]
        fields = "__all__"



"""class GoodProxy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestampAdded = models.DateTimeField(default=timezone.now)
    timestampChecked = models.DateTimeField(default=timezone.now)
    email = models.EmailField(defaudlt="")
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
        return "{1}:{2} {3} {0} {4} {5} {6}".format(self.protokol ,self.ipAdress, self.port, self.email,self.anonymitaetsLevel, self.country, self.latenz, self.timestampAdded, self.timestampChecked)
"""
