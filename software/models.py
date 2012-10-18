from django.db import models

class Software(models.Model):
    manufacturer = models.CharField(max_length=200)
    product = models.CharField(max_length=200)
    APPVYES = 'JA'
    APPVNO = 'NA'
    CHOICEAPPV = ((APPVYES, 'Yes'), (APPVNO, 'No'),)
    appv = models.CharField(max_length=5, choices=CHOICEAPPV, default=APPVYES)
    version = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)
    def __unicode__(self):
        return self.manufacturer

class Lector(models.Model):
    username = models.CharField(max_length=5)
    fullname = models.CharField(max_length=100)
    telephone = models.IntegerField()
    def __unicode__(self):
        return self.username