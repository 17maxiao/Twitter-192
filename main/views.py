from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User 

# Create your views here.

def splash_view(request):
	return render(request, "splash.html", {})

def profile_view(request):
	return render(request, "profile.html", {})

def login_view(request):
	return render(request, "login.html", {})

def home_view(request):
	return render(request, "home.html", {})

def hashtag_view(request):
	return render(request, "hashtag.html", {})

def login_account(request):
    username, password = request.POST['username'], request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('home/')
    else: 
        return redirect('/login?error=True')

def signup(request):
    user = User.objects.create_user(
        username = request.POST['username'],
        password = request.POST['password'],
        email = request.POST['email']
    )
    login(request, user)
    return redirect('home/')

def logout_view(request):
    logout(request)
    return redirect('/')

