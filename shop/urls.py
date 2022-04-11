from django.urls import path, include
import django.contrib.auth.urls
from . import views

app_name = 'shop'

urlpatterns = [
        path('', views.products.product_add, name='product_add'),
        path('product_list/', views.products.product_list, name='product_list'),

]