from django.db import models
from django.conf import settings

# Create your models here.
class installationTBL(models.Model):
    PRODUCTS = [
        ('P1','Solar Panels'),
        ('P2','EV Charging'),
        ('P3', 'EV Car'),
        ('P4', 'Solar Batteries'),
        ('P5', 'Wind Farm'),
    ]
    STATUSES = [
        ('Conf', 'Confirmed'),
        ('Canc','Cancelled'),
        ('Comp','Completed'),
        ('Pend', 'Pending'),
    ]
    installUserID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name="install_bookings")
    installDate = models.DateTimeField
    productType = models.CharField(choices=PRODUCTS)
    status = models.CharField(choices=STATUSES, default="Pend")



class consultation_TRL(models.Model):
    PRODUCTS = [
        ('A1','Solar Panels Consultation'),
        ('A2','EV Charging Consultation'),
        ('A3', 'EV Car Consultation'),
        ('A4', 'Solar Batteries Consultation'),
        ('A5', 'Wind Farm Consultation'),
    ]
    STATUSES = [
        ('Conf', 'Confirmed'),
        ('Canc','Cancelled'),
        ('Comp','Completed'),
        ('Pend', 'Pending'),
    ]   
    consultUserID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name="consult_bookings")
    consultDate = models.DateTimeField
    consultType = models.CharField(choices=PRODUCTS)
    status = models.CharField(choices=STATUSES, default="Pend")


class usageUserID(models.Model):
     usageUserID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="usage",)
     logDate = models.DateTimeField(auto_now_add=True),
     kwhConsumed = models.FloatField(default=0),
     CarbonFootprint = models.FloatField(default=0),
     