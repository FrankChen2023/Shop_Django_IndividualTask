from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'shop/index.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products' : products})

def log_in(request):
    msg = 'Please enter your username and password:'
    if request.method=='POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            msg = 'Wrong! Username or password is incorrect!'
            return render(request, 'login.html', {'msg' : msg})
    return render(request, 'login.html', {'msg': msg})

def sign_up(request):
    msg = 'Please enter your account details:'
    if request.method=='POST':
        username = request.POST.get('username', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        username_check = User.objects.filter(username=username)
        if username_check:
            msg = 'Wrong! A user with that username already exists!'
            return render(request, 'signup.html', {'msg' : msg})
        if username == '':
            msg = 'Wrong! Username cannot be empty!'
            return render(request, 'signup.html', {'msg' : msg})
        if password1 != password2:
            msg = 'Wrong! The two password fields didn’t match!'
            return render(request, 'signup.html', {'msg' : msg})
        User.objects.create_user(username=username, password=password1, email=email, address=address).save()
        return redirect('/login/')
    return render(request, 'signup.html')

def log_out(request):
    logout(request)
    return redirect('/')