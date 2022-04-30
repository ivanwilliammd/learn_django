from django.db import models

# Create your models here.
class RestaurantLocations(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200, null=True, blank=True)