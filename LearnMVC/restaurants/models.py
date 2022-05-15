from uuid import uuid4
from django.db import models
from django.db.models.signals import pre_save, post_save
from autoslug import AutoSlugField

from .utils import unique_slug_generator
from .validators import validate_category


from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your models here.
class RestaurantLocation(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True, validators = [validate_category])
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    my_date_field = models.DateField(auto_now=True)
    # slug = models.SlugField(unique=True)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name + ' - ' + self.location

    @property
    def title(self):
        return self.name

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    # print('saving..')
    # print(instance.timestamp)
    instance.category = instance.category.capitalize()
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

# def rl_post_save_receiver(sender, instance, created, *args, **kwargs):
#     print('saved')
#     print(instance.timestamp)
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)
#         instance.save()

pre_save.connect(rl_pre_save_receiver, sender=RestaurantLocation)
# post_save.connect(rl_post_save_receiver, sender=RestaurantLocation)