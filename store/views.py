from django.shortcuts import render,redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .forms import SignInForm

# Create your views here.

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html',{'products': products})

def aboutme(request):
    return render(request, 'aboutme.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            messages.success(request, ('Logged in successfully'))
            return redirect('home')
        else:
            messages.success(request, ('There was an error while logging in, please try agin.'))
            return redirect('login')
    else:
        return render(request, 'login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request, ('Logged out successfully'))
    return redirect('home')

def signin_user(request):
    form = SignInForm()
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            # login user
            user = authenticate(username = username, password = password)
            login(request,user)
            messages.success(request, ('You have registered successfully.'))
            return redirect('home')
        else:
            messages.success(request, ('There was a problem during sign in, please try again.'))
            return redirect('signin')
    else:
        return render(request, 'signin.html',{'form' : form})