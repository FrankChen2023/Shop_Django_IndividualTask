from django.shortcuts import render
from shop.models import Product

def product_search(request):
    products = Product.objects.all()
    key = 'name'
    if request.method=="POST":
        try:
            key = request.POST.get('key', 'name')
            type = request.POST.get('type', 'All')
            sort  = request.POST.get('sort', 'Unsort')
            target = request.POST.get('target', '')
            if key=='id':
                products = Product.objects.filter(id=target)
            if key=='name' and type=='All':
                products = Product.objects.filter(name__icontains=target)
            if key=='name' and type!='All':
                products = Product.objects.filter(type=type, name__icontains=target)
            if sort=='Upward':
                products = Product.objects.order_by('price')
            if sort=='Backward':
                products = Product.objects.order_by(-'price')
        except:
            pass
    return render(request, 'product/product_search.html', {'products' : products})
        