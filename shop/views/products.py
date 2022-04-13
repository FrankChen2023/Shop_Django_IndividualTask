from django.shortcuts import render
from shop.models import Product
from django.contrib.auth.decorators import login_required

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products' : products })

# Only admin could add new product.
# @login_required
def product_add(request):
    product = None
    if request.method=="POST":
        name = request.POST.get('name','')
        price = request.POST.get('price','')
        amount = request.POST.get('amount','')
        type = request.POST.get('type','')
        product = Product.objects.create(name=name, price=price, amount=amount, type=type)
        product.save()
    return render(request, 'shop/product_add.html', {'product' : product})

def product_search(request):
    products = Product.objects.all()
    key = 'name'
    if request.method=="POST":
        key = request.POST.get('key', 'name')
        target = request.POST.get('target', '')
        if key=='id':
            products = Product.objects.filter(id=target)
        if key=='name':
            products = Product.objects.filter(name__icontains=target)
    return render(request, 'shop/product_search.html', {'products' : products})
        