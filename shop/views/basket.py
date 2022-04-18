from django.shortcuts import render, redirect
from shop.models import Basket, Basket_Detail
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def basket_add(request):
    msg = ''
    judge = None
    basketname = None
    if request.method=='POST':
        username = request.user.username
        basketname = request.POST.get('basketname', '')
        name = request.POST.get('name', '')
        address = request.POST.get('address', '')
        repeat = Basket.objects.filter(basketname=basketname)
        if repeat:
            msg = 'Wrong! The basketname has existed in your baskets, please try another name!'
        elif '/' in basketname:
            msg = 'Wrong! The basketname cannot contain character "/" !'
        else:
            Basket.objects.create(username=username, basketname=basketname, name=name, address=address).save()
            judge = 1
    return render(request, 'basket/basket_add.html', {'msg': msg, 'basketname' : basketname, 'judge' : judge})

@login_required
def basket_detail(request, basketname):
    username = request.user.username
    basket = Basket.objects.get(username=username, basketname=basketname)
    items = Basket_Detail.objects.filter(username=username, basketname=basketname)
    return render(request, 'basket/basket_detail.html', {'basket' : basket, 'items' : items})

@login_required
def basket_edit(request, basketname):
    msg = ''
    username = request.user.username
    basket = Basket.objects.get(username=username, basketname=basketname)
    items = Basket_Detail.objects.filter(username=username, basketname=basketname)
    if request.method=='POST':
        basketname1 = request.POST.get('basketname', '')
        name1 = request.POST.get('name', '')
        address1 = request.POST.get('address', '')
        repeat = Basket.objects.filter(basketname=basketname1)
        if basketname1==basket.basketname:
            Basket.objects.filter(username=username, basketname=basketname).update(name=name1, address=address1)
            Basket_Detail.objects.filter(username=username, basketname=basketname).update(name=name1, address=address1)
            msg = 'Success! Now you can return back and check your modification.'
        else:
            if repeat:
                msg = 'Wrong! The basketname has existed in your baskets, please try another name!'
            elif '/' in basketname:
                msg = 'Wrong! The basketname cannot contain character "/" !'
            else:
                Basket.objects.filter(username=username, basketname=basketname).update(basketname=basketname1, name=name1, address=address1)
                Basket_Detail.objects.filter(username=username, basketname=basketname).update(basketname=basketname1, name=name1, address=address1)
                msg = 'Success! Now you can return back and check your modification.'
    return render(request, 'basket/basket_edit.html', {'msg': msg, 'basket' : basket})
