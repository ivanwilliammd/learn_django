from django.conf import settings
from django.db import models
from django.db.models.signals import post_save # ensure profile exists

# Create your models here.

User = settings.AUTH_USER_MODEL

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # user.profile
    followers = models.ManyToManyField(User, related_name='is_following', blank=True) # user.followers.all()
    # following = models.ManyToManyField(User, related_name='following', blank=True) # user.following.all()
    
    activated = models.BooleanField(default=False)
    activation_key = models.CharField(max_length=120, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        profile, is_created = Profile.objects.get_or_create(user=instance)
        default_user_profile = Profile.objects.get(user__username="admin")
        default_user_profile.followers.add(instance) # New user always following the first user
        # default_user_profile.followers.remove(instance)
        # default_user_profile.save()
        profile.followers.add(default_user_profile.user)
        profile.followers.add(2)


post_save.connect(post_save_user_receiver, sender=User)