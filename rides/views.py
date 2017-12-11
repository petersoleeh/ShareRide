from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Profile,Driver,Rides
from django.contrib import messages
from .forms import UserForm,ProfileForm,DriverForm,VehicleForm
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.contrib.auth.models import User
from .forms import DriverForm,RideForm

# Create your views here.
@login_required(login_url='/accounts/register')
def index(request):
    return render(request,'index.html')


@login_required(login_url='/accounts/login')
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'all-rides/user_driver.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required(login_url='/accounts/register')
def profile(request):
    driver = Driver.objects.all()

    return render(request,'all-rides/user_driver.html',{"driver":driver})


@login_required(login_url='/accounts/register')
def rider(request):
    rides=Rides.objects.all()
    current_user = request.user
    if request.method == 'POST':
        form = RideForm(request.POST,request.FILES)
        if form.is_valid():
            rides = form.save(commit=False)
            rides.user = current_user
            print(rides.user)
            rides.save()

    else:
        form = RideForm()

    return render(request,'all-rides/rider.html',{"rides":rides,"form":form})


@login_required(login_url='/accounts/login')
def update_car(request):
    cars = Driver.objects.all()
    current_user = request.user
    if request.method == 'POST':
        form = DriverForm(request.POST,request.FILES)
        if form.is_valid():
            cars=form.save(commit=False)
            cars.user = current_user
            cars.save()
    else:
        form = DriverForm()




    return render(request,'all-rides/update_car.html',{"form":form,"cars":cars})

@login_required(login_url='/accounts/login')
def new_car(request):
    cars = Driver.objects.all()
    current_user = request.user
    if request.method == 'POST':
        form = VehicleForm(request.POST,request.FILES)
        if form.is_valid():
            cars=form.save(commit=False)
            cars.user = current_user
            cars.save()


    else:
        form = VehicleForm()



    return render(request,'all-rides/new_car.html',{"form":form,"cars":cars})
