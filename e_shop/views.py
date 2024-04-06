from django.shortcuts import render, redirect
from .models import Product

# login
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

#register

from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib.auth import login as auth_login
# Create your views here.

products = Product.objects.all()
def index(request):
    return render(request, 'index.html',
                  {'products':products})

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def login_user(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username = username, password = password)
        if user is not None:
            login(request,user)
            messages.success(request, ("You've been loggedin successfully! "))
            return redirect('index')

        else:
            messages.success(request, ("Incorrect password or username! "))
            return redirect('login')
    
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You've been logged out"))
    return redirect('index')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log in user
            auth_login(request, user)
            messages.success(request, "User registration successful. You are now logged in.")
            return redirect('index')
        else:
            messages.error(request, "Registration failed. Please correct the errors.")
    return render(request, 'register.html', {'form': form})