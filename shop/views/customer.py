from django.shortcuts import render, redirect
from shop.models import Customer, Basket
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def customer_balance(request):
    username = request.user.username
    current_user = Customer.objects.get(username=username)
    baskets = Basket.objects.filter(username=username)
    return render(request, 'customer/customer_balance.html', {'current_user' : current_user, 'baskets' : baskets})

