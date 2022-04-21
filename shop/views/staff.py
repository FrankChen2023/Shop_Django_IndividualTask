from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from shop.models import Product, Customer, Basket, Basket_Detail
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def admin_console(request):
    return render(request, 'staff/admin_console.html')

@staff_member_required
def staff_customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'staff/staff_customer_list.html', {'customers' : customers})

@staff_member_required
def staff_customer_detail(request, id):
    msg = ''
    customer = Customer.objects.get(id=id)
    if request.method=="POST":
        email = request.POST.get('email')
        balance = request.POST.get('balance')
        Customer.objects.filter(id=id).update(email=email, balance=balance)
        msg = 'Success!'
    customer = Customer.objects.get(id=id)
    return render(request, 'staff/staff_customer_detail.html', {'customer' : customer, 'msg' : msg})

@staff_member_required
def staff_customer_delete(request, id):
    msg = ''
    customer = Customer.objects.get(id=id)
    judge = 'admin001' + '/' + customer.username
    if request.method=='POST':
        confirm = request.POST.get('confirm')
        if judge==confirm:
            items = Basket_Detail.objects.filter(username=customer.username)
            for item in items:
                product = Product.objects.get(id=item.item_id)
                Product.objects.filter(id=item.item_id).update(amount=product.amount+item.amount)
            Basket_Detail.objects.filter(username=customer.username).delete()
            Basket.objects.filter(username=customer.username).delete()
            User.objects.get(username=customer.username).delete()
            Customer.objects.get(username=customer.username).delete()
            return redirect('/staff_customer_delete_success/')
        else:
            msg = 'Wrong type! Please confirm and type again.'
    return render(request, 'staff/staff_customer_delete.html', {'customer' : customer, 'msg' : msg})

@staff_member_required
def staff_customer_delete_success(request):
    return render(request, 'staff/staff_customer_delete_success.html')

@staff_member_required
def staff_basket_list(request, username):
    baskets = Basket.objects.filter(username=username)
    return render(request, 'staff/staff_basket_list.html', {'baskets' : baskets})

@staff_member_required
def staff_basket_detail(request, id):
    msg = ''
    basket = Basket.objects.get(id=id)
    if request.method=="POST":
        basketname = request.POST.get('basketname')
        repeat = Basket.objects.filter(username=basket.username, basketname=basketname)
        name = request.POST.get('name')
        address = request.POST.get('address')
        status = request.POST.get('status')
        if status != 'paid' and status != 'unpaid':
            msg = 'Wrong! Status value can only be "paid" or "unpaid".'
            return render(request, 'staff/staff_basket_detail.html', {'basket' : basket, 'msg' : msg})
        if basketname!=basket.basketname and repeat:
            msg = 'Wrong! The basketname is repeated in the customer baskets.'
            return render(request, 'staff/staff_basket_detail.html', {'basket' : basket, 'msg' : msg})
        Basket.objects.filter(id=id).update(basketname=basketname, name=name, address=address, status=status)
        msg = 'Success!'
    basket = Basket.objects.get(id=id)
    return render(request, 'staff/staff_basket_detail.html', {'basket' : basket, 'msg' : msg})

@staff_member_required
def staff_basket_delete(request, id):
    msg = ''
    basket = Basket.objects.get(id=id)
    judge = 'admin001' + '/' + basket.username + '/' + basket.basketname
    if request.method=='POST':
        confirm = request.POST.get('confirm')
        if judge==confirm:
            items = Basket_Detail.objects.filter(username=basket.username, basketname=basket.basketname)
            for item in items:
                product = Product.objects.get(id=item.item_id)
                Product.objects.filter(id=item.item_id).update(amount=product.amount+item.amount)
            Basket_Detail.objects.filter(username=basket.username, basketname=basket.basketname).delete()
            Basket.objects.filter(username=basket.username, basketname=basket.basketname).delete()
            return redirect('shop:staff_basket_delete_success', username=basket.username})
        else:
            msg = 'Wrong type! Please confirm and type again.'
    return render(request, 'staff/staff_basket_delete.html', {'basket' : basket, 'msg' : msg})

@staff_member_required
def staff_basket_delete_success(request, username):
    return render(request, 'staff/staff_customer_delete_success.html', {'username' : username})

@staff_member_required
def staff_order_list(request, username, basketname):
    items = Basket_Detail.objects.filter(username=username, basketname=basketname)
    return render(request, 'staff/staff_order_list.html', {'items' : items})

@staff_member_required
def staff_order_detail(request, id):
    msg = ''
    item = Basket_Detail.objects.get(id=id)
    product = Product.objects.get(id=item.item_id)
    total_amount = item.amount+product.amount
    if request.method=="POST":
        price = request.POST.get('price')
        amount = int(request.POST.get('amount'))
        Product.objects.filter(id=item.item_id).update(amount=total_amount-amount)
        Basket_Detail.objects.filter(id=id).update(price=price, amount=amount)
        item = Basket_Detail.objects.get(id=id)
        Basket_Detail.objects.filter(id=id).update(total_price=item.price*item.amount)
        msg = 'Success!'
    item = Basket_Detail.objects.get(id=id)
    return render(request, 'staff/staff_order_detail.html', {'item' : item, 'product' : product, 'total_amount' : total_amount, 'msg' : msg})

@staff_member_required
def staff_order_delete(request, id):
    msg = ''
    item = Basket_Detail.objects.get(id=id)
    judge = 'admin001' + '/' + item.username + '/' + item.basketname + '/order' 
    if request.method=='POST':
        confirm = request.POST.get('confirm')
        if judge==confirm:
            product = Product.objects.get(id=item.item_id)
            Product.objects.filter(id=item.item_id).update(amount=product.amount+item.amount)
            Basket_Detail.objects.filter(id=id).delete()
            return redirect('shop:staff_order_delete_success', username=item.username, basketname=item.basketname)
        else:
            msg = 'Wrong type! Please confirm and type again.'
    return render(request, 'staff/staff_order_delete.html', {'item' : item, 'msg' : msg})

@staff_member_required
def staff_order_delete_success(request, username, basketname):
    return render(request, 'staff/staff_order_delete_success.html', {'username' : username, 'basketname' : basketname})

@staff_member_required
def staff_product_list(request):
    products = Product.objects.all()
    return render(request, 'staff/staff_product_list.html', {'products' : products})

@staff_member_required
def staff_customer_list_total(request):
    customers = Customer.objects.all()
    key = 'username'
    if request.method=="POST":
        try:
            key = request.POST.get('key', 'username')
            target = request.POST.get('target', '')
            if key=='id':
                customers = Customer.objects.filter(id=target)
            if key=='username':
                customers = Customer.objects.filter(username__icontains=target)
        except:
            pass
    return render(request, 'staff/staff_customer_list_total.html', {'customers' : customers})

@staff_member_required
def staff_basket_list_total(request):
    baskets = Basket.objects.all()
    if request.method=="POST":
        try:
            username = request.POST.get('username', '')
            baskets = Basket.objects.filter(username__icontains=username)
        except:
            pass
    return render(request, 'staff/staff_basket_list_total.html', {'baskets' : baskets})

@staff_member_required
def staff_order_list_total(request):
    items = Basket_Detail.objects.all()
    key = 'itemname'
    if request.method=="POST":
        try:
            key = request.POST.get('key', 'itemname')
            target = request.POST.get('target', '')
            if key=='itemname':
                items = Basket_Detail.objects.filter(item_id__icontains=target)
            if key=='username':
                items = Basket_Detail.objects.filter(username__icontains=target)
        except:
            pass
    return render(request, 'staff/staff_order_list_total.html', {'items' : items})

@staff_member_required
def staff_product_add(request):
    product = None
    if request.method=="POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        amount = request.POST.get('amount')
        type = request.POST.get('type')
        product = Product.objects.create(name=name, price=price, amount=amount, type=type)
        product.save()
    return render(request, 'staff/staff_product_add.html', {'product' : product})

@staff_member_required
def staff_product_edit(request):
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
    return render(request, 'staff/staff_product_edit.html', {'products' : products})

@staff_member_required
def staff_product_detail(request, id):
    msg = ''
    product = Product.objects.get(id=id)
    if request.method=="POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        amount = request.POST.get('amount')
        type = request.POST.get('type')
        Product.objects.filter(id=id).update(name=name, price=price, amount=amount, type=type)
        msg = 'Success!'
    product = Product.objects.get(id=id)
    return render(request, 'staff/staff_product_detail.html', {'product' : product, 'msg' : msg})

@staff_member_required
def staff_product_delete(request, id):
    msg = ''
    product = Product.objects.get(id=id)
    judge = 'admin001' + '/' + str(product.id)
    if request.method=='POST':
        confirm = request.POST.get('confirm')
        if judge==confirm:
            Basket_Detail.objects.filter(item_id=id).delete()
            Product.objects.filter(id=id).delete()
            return redirect('/staff_product_delete_success/')
        else:
            msg = 'Wrong type! Please confirm and type again.'
    return render(request, 'staff/staff_product_delete.html', {'product' : product, 'msg' : msg})

@staff_member_required
def staff_product_delete_success(request):
    return render(request, 'staff/staff_product_delete_success.html')