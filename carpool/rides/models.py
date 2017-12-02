from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500,blank=True)
    phone_number = models.IntegerField(blank=True,null=True)
    pro_pic = models.ImageField(upload_to = 'rides/',blank=True,null=True)

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_user_profile(sender,instance, **kwargs):
    instance.profile.save()
