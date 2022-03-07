from django.db import models


# Create your models here.


# Create your models here.
class Address(models.Model):
    address = models.CharField(max_length=500, blank=True, null=True)
    apartment = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.IntegerField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.address


class Configuration(models.Model):
    dark_mode = models.BooleanField(default=False, null=True, blank=True)
    location = models.BooleanField(default=False, null=True, blank=True)
    new_trips_notifications = models.BooleanField(default=False, null=True, blank=True)
    notification = models.BooleanField(default=False, null=True, blank=True)
    storage = models.BooleanField(default=False, null=True, blank=True)
