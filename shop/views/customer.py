from django.shortcuts import render, redirect
from shop.models import Product, Customer, Basket
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def customer_balance(request):
    username = request.user.username
    current_user = Customer.objects.get(username=username)
    baskets = Basket.objects.filter(username=username)
    return render(request, 'shop/customer_balance.html', {'current_user' : current_user, 'baskets' : baskets})

@login_required
def basket_add(request):
    msg = 'Please modify the details of your new basket:'
    if request.method=='POST':
        username = request.user.username
        basketname = request.POST.get('basketname', '')
        name = request.POST.get('name', '')
        address = request.POST.get('address', '')
        repeat = Basket.objects.filter(basketname=basketname)
        if repeat:
            msg = 'Wrong! The basketname has existed in your baskets, please try another name!'
        else:
            Basket.objects.create(username=username, basketname=basketname, name=name, address=address).save()
            return redirect('/basket_success/')
    return render(request, 'shop/basket_add.html', {'msg': msg})