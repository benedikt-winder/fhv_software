from django.db import models

class Software(models.Model):
    manufacturer = models.CharField(max_length=200)
    product = models.CharField(max_length=200)
    appv = models.CharField(max_length=200)
    version = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)
    def __unicode__(self):
        return self.manufacturer

class Lector(models.Model):
    username = models.CharField(max_length=5)
    def __unicode__(self):
        return self.username