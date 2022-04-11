from django.shortcuts import redirect, render
from django.utils import timezone
from shop.models import Product
from django.contrib.auth.decorators import login_required

def product_list(request):
    Product.objects.create(name='banana', price='3.99', amount='99', type='Food').save()
    products = Product.objects.all()    
    return render(request, 'shop/product_list.html', {'products' : products })

# Only admin could add new product.
# @login_required
def product_add(request):
    if request.method=="POST":
        name = request.POST.get('name','')
        price = request.POST.get('price','')
        amount = request.POST.get('amount','')
        type = request.POST.get('type','')
        Product.objects.create(name=name, price=price, amount=amount, type=type).save()
    return render(request, 'shop/product_add.html')