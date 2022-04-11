from django.shortcuts import redirect, render
from django.utils import timezone
from shop.models import Product
from django.contrib.auth.decorators import login_required

def product_list(request):
    products = Product.objects.all()    
    return render(request, 'shop/product_list.html', {'products' : products })

# Only admin could add new product.
# @login_required
def product_add(request):
    if request.method=="POST":
        name = request.POST.get('name','apple')
        price = request.POST.get('price','1.99')
        amount = request.POST.get('amount','99')
        type = request.POST.get('type','Food')
        Product.objects.create(name=name, price=price, amount=amount, type=type).save()
    return render(request, 'shop/product_add.html')