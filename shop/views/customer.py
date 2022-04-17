from django.shortcuts import render, redirect
from shop.models import Product, Customer, Basket, Basket_Detail
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
            return redirect('shop:item_add', basketname=basketname)
    return render(request, 'shop/basket_add.html', {'msg': msg})

def basket_success(request):
    return render(request, 'shop/basket_success.html')

@login_required
def item_add(request, basketname):
    products = Product.objects.all()
    key = 'name'
    if request.method=="POST" and 'key' in request.POST:
        key = request.POST.get('key', 'name')
        target = request.POST.get('target', '')
        if key=='id':
            products = Product.objects.filter(id=target)
        if key=='name':
            products = Product.objects.filter(name__icontains=target)
    return render(request, 'shop/item_add.html', {'products' : products, 'basketname' : basketname})

@login_required
def item_list(request):
    items = Basket_Detail.objects.all()
    return render(request, 'shop/item_list.html', {'items' : items})

@login_required
def item_detail(request, basketname, id):
    msg = ''
    product = Product.objects.get(id=id)
    username = request.user.username
    current_basket = Basket.objects.get(username=username, basketname=basketname)
    if request.method=='POST':
        item_amount = int(request.POST.get('amount'))
        item = Product.objects.get(id=id)
        Basket_Detail.objects.create(username=username, basketname=basketname, name=current_basket.name,
        address=current_basket.address, item=item.name, price=item.price, amount=item_amount, 
        total_price=item.price*item_amount).save()
        msg = 'Success! The item has been added into your basket!'
        Product.objects.filter(id=id).update(amount=product.amount-item_amount)
        product = Product.objects.get(id=id)
    return render(request, 'shop/item_detail.html', {'msg' : msg, 'product' : product, 'basketname' : basketname})

@login_required
def basket_detail(request, basketname):
    username = request.user.username
    basket = Basket.objects.get(username=username, basketname=basketname)
    items = Basket_Detail.objects.filter(username=username, basketname=basketname)
    return render(request, 'shop/basket_detail.html', {'basket' : basket, 'items' : items})

