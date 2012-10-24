from django.db import models

class Software(models.Model):
    sw_id = models.AutoField(primary_key=True)
    manufacturer = models.CharField(max_length=200)
    product = models.CharField(max_length=200)
    APPVDROPDOWN = (('Yes', 'Yes'), ('No', 'No'))
    appv = models.CharField(max_length=3, choices=APPVDROPDOWN)
    version = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)
    # For the output for the Reports
    def __unicode__(self):
        return '%s %s (%s) %s' %(self.manufacturer, self.product, self.version, self.appv)

class Lector(models.Model):
    lector_id = models.AutoField(primary_key=True)
    software = models.ForeignKey(Software)
    username = models.CharField(max_length=5)
    fullname = models.CharField(max_length=100)
    telephone = models.IntegerField()
    # For the output for the Reports
    def __unicode__(self):
        return '%s - %s - %s' %(self.username, self.fullname, self.software)

