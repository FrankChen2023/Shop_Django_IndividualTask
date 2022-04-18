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
def basket_edit(request, id):
    msg = ''
    username = request.user.username
    basket = Basket.objects.get(id=id)
    items = Basket_Detail.objects.filter(username=username, basketname=basket.basketname)
    if request.method=='POST':
        basketname = request.POST.get('basketname', '')
        name = request.POST.get('name', '')
        address = request.POST.get('address', '')
        repeat = Basket.objects.filter(basketname=basketname)
        if basketname==basket.basketname:
            Basket.objects.filter(id=id).update(name=name, address=address)
            Basket_Detail.objects.filter(username=username, basketname=basket.basketname).update(name=name, address=address)
            msg = 'Success! Now you can return back and check your modification.'
            basket = Basket.objects.get(username=username, basketname=basketname)
        else:
            if repeat:
                msg = 'Wrong! The basketname has existed in your baskets, please try another name!'
            elif '/' in basketname:
                msg = 'Wrong! The basketname cannot contain character "/" !'
            else:
                Basket.objects.filter(id=id).update(basketname=basketname, name=name, address=address)
                Basket_Detail.objects.filter(username=username, basketname=basket.basketname).update(basketname=basketname, name=name, address=address)
                msg = 'Success! Now you can return back and check your modification.'
                basket = Basket.objects.get(username=username, basketname=basketname)
    return render(request, 'basket/basket_edit.html', {'msg': msg, 'basket' : basket, 'id' : id})

def basket_delete(request, id):
    basket = Basket.objects.get(id=id)
    judge = basket.username + '/' + basket.basketname
    if request.method=='POST':
        confirm = request.POST.get('confirm')
        if judge==confirm:
            Basket.objects.get(id=id).delete()
            items = Basket_Detail.objects.filter(username=basket.username, basketname=basket.basketname)
            for item in items:
                product = Product.objects.filter(id=item.item_id)
                Product.objects.filter(id=item.item_id).update(amount=product.amount+item.amount)
                Basket_Detail.objects.filter(id=item.id).delete()
            return redirect('shop:/basket_delete_success/')
    return render(request, 'basket/basket_delete.html', {'basket' : basket})

def basket_delete_success(request):
    return render(request, 'basket/basket_delete_success.html')


