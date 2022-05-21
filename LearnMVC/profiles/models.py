from django.conf import settings
from django.db import models
from django.db.models.signals import post_save # ensure profile exists
from django.core.mail import send_mail
# Create your models here.

from .utils import code_generator

User = settings.AUTH_USER_MODEL


class ProfileManager(models.Manager):
    def toggle_follow(self, request_user, user_to_toggle):
        profile_ = Profile.objects.get(user__username__iexact=user_to_toggle)
        user = request_user

        is_following = False
        if user in profile_.followers.all():
            profile_.followers.remove(user)
        else:
            profile_.followers.add(user)
            is_following = True
        return profile_, is_following

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # user.profile
    followers = models.ManyToManyField(User, related_name='is_following', blank=True) # user.followers.all()
    # following = models.ManyToManyField(User, related_name='following', blank=True) # user.following.all()
    
    activated = models.BooleanField(default=False)
    activation_key = models.CharField(max_length=120, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = ProfileManager()

    def __str__(self):
        return self.user.username
    
    def send_activation_email(self):
        print("Activation email")
        if not self.activated:
            self.activation_key = code_generator()
            self.save()

            subject = 'Activate Account'
            from_email = settings.DEFAULT_FROM_EMAIL
            message = f'Activate your account here : {self.activation_key}'
            recipient_list = [self.user.email]
            html_message = f'<p>Activate your account here : {self.activation_key}</p>'
            print(subject, message, from_email, recipient_list, html_message)
            sent_mail = send_mail(subject, message, from_email, recipient_list, fail_silently=False, html_message=html_message)
            return sent_mail

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