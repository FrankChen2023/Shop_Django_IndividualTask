from django.shortcuts import render, redirect
from shop.models import Product, Basket, Basket_Detail
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def item_add(request, basketname):
    products = Product.objects.all()
    key = 'name'
    if request.method=="POST":
        try:
            key = request.POST.get('key', 'name')
            type = request.POST.get('type', 'All')
            target = request.POST.get('target', '')
            if key=='id':
                products = Product.objects.filter(id=target)
            if key=='name' and type=='All':
                products = Product.objects.filter(name__icontains=target)
            if key=='name' and type!='All':
                products = Product.objects.filter(type=type, name__icontains=target)
        except:
            pass
    return render(request, 'item/item_add.html', {'products' : products, 'basketname' : basketname})

@login_required
def item_list(request):
    items = Basket_Detail.objects.all()
    return render(request, 'item/item_list.html', {'items' : items})

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
    return render(request, 'item/item_detail.html', {'msg' : msg, 'product' : product, 'basketname' : basketname})

