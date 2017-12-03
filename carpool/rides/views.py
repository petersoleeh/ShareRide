from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages
from .forms import UserForm,ProfileForm
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request,'index.html')



# @login_required
@transaction.atomic
def update_profile(request,username):
    user = User.objects.get(username=username)
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
    return render(request, 'all-rides/user_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

# @login_required(login_url='/accounts/login')
def profile(request):
    # try:
    #     user = User.objects.get(username=username)
    #
    #     profile = Profile.objects.filter(user_id=user).all()
    #
    # except Profile.DoesNotExist:
    #     raise Http404()

    return render(request,'all-rides/user_profile.html')
