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


    def __str__(self):
        return self.user.user.username


    @receiver(post_save,sender=User)
    def create_user_profile(sender,instance,created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save,sender=User)
    def save_user_profile(sender,instance, **kwargs):
        instance.profile.save()



class Rides(models.Model):
    source = models.CharField(max_length=255)
    dest = models.CharField(max_length=255)
    ride_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.source + ' to ' +self.dest


class Review(models.Model):
    commenter = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField(max_length=255,blank=True)
    comment_date = models.DateTimeField(auto_now_add=True)
