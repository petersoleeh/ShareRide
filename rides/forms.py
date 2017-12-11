from .models import Profile,Driver,Rides
from django import forms
from django.contrib.auth.models import User



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'phone_number', 'pro_pic',)

class DriverForm(forms.ModelForm):
    class Meta:
        model=Driver
        fields = ('car_pic','car_make','seats','reg_numb',)


class VehicleForm(forms.ModelForm):
    class Meta:
        model =Driver
        fields=('car_make','car_pic','car_model','reg_numb','seats',)

class RideForm(forms.ModelForm):
    class Meta:
        model = Rides
        fields=('source','dest',)
