from django.conf import settings
from django.db import models
from django.utils import timezone


class installationTBL(models.Model):
    PRODUCTS = [
        ('P1', 'Solar Panels'),
        ('P2', 'EV Charging'),
        ('P3', 'EV Car'),
        ('P4', 'Solar Batteries'),
        ('P5', 'Wind Farm'),
    ]
    STATUSES = [
        ('Conf', 'Confirmed'),
        ('Canc', 'Cancelled'),
        ('Comp', 'Completed'),
        ('Pend', 'Pending'),
    ]
    installUserID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="install_bookings")
    installDate = models.DateTimeField(default=timezone.now)
    productType = models.CharField(max_length=10, choices=PRODUCTS)
    status = models.CharField(max_length=10, choices=STATUSES, default="Pend")


class consultation_TRL(models.Model):
    PRODUCTS = [
        ('A1', 'Solar Panels Consultation'),
        ('A2', 'EV Charging Consultation'),
        ('A3', 'EV Car Consultation'),
        ('A4', 'Solar Batteries Consultation'),
        ('A5', 'Wind Farm Consultation'),
    ]
    STATUSES = [
        ('Conf', 'Confirmed'),
        ('Canc', 'Cancelled'),
        ('Comp', 'Completed'),
        ('Pend', 'Pending'),
    ]
    consultUserID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="consult_bookings")
    consultDate = models.DateTimeField(default=timezone.now)
    consultType = models.CharField(max_length=10, choices=PRODUCTS)
    status = models.CharField(max_length=10, choices=STATUSES, default="Pend")


class usageUserID(models.Model):
    usageUserID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="usage")
    logDate = models.DateTimeField(default=timezone.now)
    kwhConsumed = models.FloatField(default=0)
    CarbonFootprint = models.FloatField(default=0)


class StorePurchase(models.Model):
    PRODUCT_CHOICES = [
        ('solar-panels', 'Solar Panels'),
        ('electric-cars', 'Electric Cars'),
        ('wind-farms', 'Wind Farms'),
    ]

    ORDER_STATUSES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="store_purchases", null=True, blank=True)
    product = models.CharField(max_length=50, choices=PRODUCT_CHOICES)
    quantity = models.PositiveIntegerField(default=1)
    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    location = models.CharField(max_length=200)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=ORDER_STATUSES, default='pending')

    def __str__(self):
        return f"{self.full_name} - {self.get_product_display()}"
