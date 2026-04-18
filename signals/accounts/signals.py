from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import *

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user = instance)
        
@receiver(post_save, sender=User)
def update(sender, instance, created, **kwargs):
    if not created:
        Profile.objects.get_or_create(user = instance)