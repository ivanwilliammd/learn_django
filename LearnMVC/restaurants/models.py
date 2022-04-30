from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    category = models.CharField(max_length=50)
    def __str__(self):
        return self.name