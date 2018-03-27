from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .forms import *

def account_login(request):
    if request.method=='POST':
        form = login_form(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
            if user is not None:
                auth.login(request, user)
                messages.success(request, "You have successfully logged in!")
                return redirect("home")
            else:
                form.add_error(None, "Your username or password was not recognised")
    else:
        form = login_form()
    return render(request, 'accounts/login.html', { 'form': form })
    
    
@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect('home')


def account_profile(request):
    return render(request, "accounts/profile.html")


def register_new_account(request):
    if request.method == 'POST':
        form = new_user_form(request.POST)
        if form.is_valid():
            form.save()
            user = auth.authenticate(username=request.POST.get('username'), password=request.POST.get('password1'))
            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect('profile')
            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        form = new_user_form()
    return render(request, 'accounts/register.html', {'form': form})