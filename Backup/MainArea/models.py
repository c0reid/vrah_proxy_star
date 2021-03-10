from django.db import models


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
