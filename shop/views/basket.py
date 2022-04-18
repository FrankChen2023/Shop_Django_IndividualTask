from django.shortcuts import render, redirect
from shop.models import Basket, Basket_Detail
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


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
            return redirect('shop:basket_success', basketname=basketname)
    return render(request, 'basket/basket_add.html', {'msg': msg})

def basket_success(request, basketname):
    return render(request, 'basket/basket_success.html', {'basketname' : basketname})

@login_required
def basket_detail(request, basketname):
    username = request.user.username
    basket = Basket.objects.get(username=username, basketname=basketname)
    items = Basket_Detail.objects.filter(username=username, basketname=basketname)
    return render(request, 'basket/basket_detail.html', {'basket' : basket, 'items' : items})