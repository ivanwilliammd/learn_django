from unicodedata import category
from django.db import models

# Create your models here.
class RestaurantLocation(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    my_date_field = models.DateField(auto_now=True)
    def __str__(self):
        return self.name + ' - ' + self.location