from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Q, signals

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500,blank=True)
    phone_number = models.IntegerField(blank=True,null=True)
    pro_pic = models.ImageField(upload_to = 'rides/',blank=True,null=True)


    def __str__(self):
        return self.user

User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])



@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)


@receiver(post_save,sender=User)
def save_user_profile(sender,instance, **kwargs):
    instance.profile.save()





class Rides(models.Model):
    source = models.CharField(max_length=255)
    dest = models.CharField(max_length=255)
    ride_date = models.DateTimeField(auto_now_add=True)
    rider = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    phone_number=models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.source + ' to ' +self.dest


class Review(models.Model):
    commenter = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField(max_length=255,blank=True)
    comment_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.comment


class Driver(models.Model):
    car_pic = models.ImageField(upload_to='driver/',blank=True)
    car_make = models.CharField(max_length=30)
    car_model= models.CharField(max_length=30)
    seats = models.IntegerField(blank=True,null=True)
    reg_numb = models.CharField(max_length=30)
    driver = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.reg_numb
