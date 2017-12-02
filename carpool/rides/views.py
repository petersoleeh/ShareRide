from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.
@login_required
def index(request):
    return render(request,'index.html')


def profile(request):
    return render(request,'all-rides/user_profile.html')
