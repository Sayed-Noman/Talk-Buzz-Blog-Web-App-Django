from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from django.views.decorators.csrf import csrf_protect

@csrf_protect
@receiver(post_save, sender=User)
def create_profile(sender, instance, created,*args, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@csrf_protect
@receiver(post_save, sender=User)
def save_profile(sender, instance,*args, **kwargs):
    instance.profile.save()