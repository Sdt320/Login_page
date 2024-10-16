from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.cache import never_cache
# Create your views here.
@login_required
@never_cache
def home(request):
    return render(request, "home.html",{})

@never_cache
def authView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Signup successful! Please log in.")
            return redirect('/accounts/login/')
        else:
            messages.warning(request, "Signup failed. Please valid information ")  
    else:
        form = UserCreationForm()  
        
    return render(request, "registration/signup.html", {"form": form})

@never_cache
def logoutview(request):
    logout(request)
    return redirect('/accounts/login/')
@login_required
def welcome(request):
    
    return render(request,'welcome.html')
