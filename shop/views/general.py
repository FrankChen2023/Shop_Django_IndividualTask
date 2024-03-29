from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from shop.models import Customer

def index(request):
    return render(request, 'shop/index.html')

def log_in(request):
    msg = 'Please enter your username and password:'
    if request.method=='POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/login_success/')
        else:
            msg = 'Wrong! Username or password is incorrect!'
    return render(request, 'log_in.html', {'msg': msg})

def sign_up(request):
    msg = 'Please enter your account details:'
    if request.method=='POST':
        username = request.POST.get('username', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        email = request.POST.get('email', '')
        username_check = User.objects.filter(username=username)
        if username_check:
            msg = 'Wrong! A user with that username already exists!'
            return render(request, 'sign_up.html', {'msg' : msg})
        if '/' in username:
            msg = 'Wrong! The username cannot contain character "/"!'
            return render(request, 'sign_up.html', {'msg' : msg})
        if password1 != password2:
            msg = 'Wrong! The two password fields didn’t match!'
            return render(request, 'sign_up.html', {'msg' : msg})
        User.objects.create_user(username=username, password=password1, email=email).save()
        Customer.objects.create(username=username, email=email, balance=10000).save()
        return redirect('/signup_success/')
    return render(request, 'sign_up.html')

def login_success(request):
    return render(request, 'login_success.html')

def signup_success(request):
    return render(request, 'signup_success.html')

def log_out(request):
    logout(request)
    return render(request, 'log_out.html')