from django.shortcuts import render
from shop.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products' : products})


@login_required
def product_add(request):
    product = None
    if request.method=="POST":
        name = request.POST.get('name','')
        price = request.POST.get('price','')
        amount = request.POST.get('amount','')
        type = request.POST.get('type','')
        product = Product.objects.create(name=name, price=price, amount=amount, type=type)
        product.save()
    return render(request, 'product/product_add.html', {'product' : product})

def product_search(request):
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
    return render(request, 'product/product_search.html', {'products' : products})
        